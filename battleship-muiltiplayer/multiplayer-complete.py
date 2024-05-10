from microbit import *
import music
import radio
import random


PLAYER = 7
SHIP = 9
WATER = 2
THRESHOLD = 400
GROUP = 23


class Sea:
    """
    Holds the state of the game board.
    """

    def __init__(self, ships=[4, 3, 2]):
        """
        Initialize the game board with the given ships.
        """
        self.board = [[WATER] * 5 for _ in range(5)]
        self.populate_board(ships)

    def near_ships(self, row, col):
        """
        Check if there are ships surrounding the given coordinates.
        """
        if row > 4 or col > 4:
            return False

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < 5 and 0 <= j < 5 and (i != row or j != col):
                    if self.board[i][j] == SHIP:
                        return False
        return True

    def possible(self, row, col, size, orientation):
        """
        Check if it is possible to place a ship.

        The ship must not be near other ships and must fit in the board.
        """
        for i in range(size):
            if orientation == "H":
                if not self.near_ships(row, col + i):
                    return False
            elif orientation == "V":
                if not self.near_ships(row + i, col):
                    return False
        return True

    def place_ship(self, size):
        """
        Place a ship of the given size in the board.

        The ship will be placed in a random available coordinate.
        The orientation can be horizontal or vertical.
        """
        available_coordinates = [
            (row, col)
            for row in range(5)
            for col in range(5)
            if self.board[row][col] == WATER
        ]

        while available_coordinates:
            row, col = random.choice(available_coordinates)
            available_coordinates.remove((row, col))

            orientation = random.choice(["H", "V"])

            if self.possible(row, col, size, orientation):
                break
        else:
            return False

        for i in range(size):
            if orientation == "H":
                self.board[row][col + i] = SHIP
            elif orientation == "V":
                self.board[row + i][col] = SHIP

        return True

    def populate_board(self, ships):
        """
        Place all the ships on the board.

        If it is not possible to place all the ships, try again.
        """
        while True:
            placed_ships = [self.place_ship(ship) for ship in ships]

            if all(placed_ships):
                break

            self.board = [[WATER] * 5 for _ in range(5)]

    def hit(self, row, col):
        """
        Check if there is a ship in the given coordinates.
        """
        return self.board[row][col] == SHIP

    def show(self):
        """
        Show the game board.
        """
        display.show(
            Image(
                ":".join(["".join(str(point) for point in line) for line in self.board])
            )
        )

    def blink(self, row, col):
        """
        Blink the given coordinates.

        This is used to show the result of a shot.
        """
        for _ in range(3):
            display.set_pixel(col, row, PLAYER)
            sleep(500)
            display.set_pixel(col, row, self.board[row][col])
            sleep(500)


class Player:
    """
    Holds the state of the player board.
    """

    def __init__(self):
        """
        Initialize the player board.
        """
        self.shots = [[0] * 5 for _ in range(5)]

        self.row = 2
        self.col = 2

        self.player_number = ""

    def show(self):
        """
        Show the player board.
        """
        display.show(
            Image(
                ":".join(["".join(str(point) for point in line) for line in self.shots])
            )
        )

    def shoot(self):
        """
        Shoot the board.

        The player can move the cursor with the accelerometer.
        The player can shoot by pressing the A button.

        The coordinates are stored for future reference.
        """
        while not button_a.is_pressed():
            self.show()

            if accelerometer.get_x() > THRESHOLD:
                self.col = min(self.col + 1, 4)
            elif accelerometer.get_x() < -THRESHOLD:
                self.col = max(self.col - 1, 0)

            if accelerometer.get_y() > THRESHOLD:
                self.row = min(self.row + 1, 4)
            elif accelerometer.get_y() < -THRESHOLD:
                self.row = max(self.row - 1, 0)

            self.blink(self.row, self.col)

    def mark(self, row, col, hit):
        """
        Mark the player board with result of a shot.
        """
        if hit:
            self.shots[row][col] = SHIP
        else:
            self.shots[row][col] = WATER

    def blink(self, row, col):
        """
        Blink the given coordinates.

        This is used to show the current coordinates of the player.
        """
        display.set_pixel(col, row, self.shots[row][col])
        sleep(50)
        display.set_pixel(col, row, PLAYER)
        sleep(50)


class Game:
    """
    Holds the state of the game.
    """

    def __init__(self):
        """
        Initialize the game.

        Create the game board and the player boards.
        Each player will have a board to place the ships and a board to make the shots.
        """
        self.sea = Sea()
        self.me = Player()
        self.opponent = Player()

        self.winner = ""

        radio.on()
        radio.config(group=GROUP)

    def start(self):
        """
        Routine to start the game.
        """
        display.show(Image.TARGET)
        music.play(music.ENTERTAINER)
        while not (button_a.is_pressed() and button_b.is_pressed()):
            display.clear()
            sleep(350)
            display.show(Image.TARGET)
            sleep(350)

        for number in "321":
            display.show(number)
            music.play(music.BA_DING)
            sleep(1000)
        music.play(music.JUMP_UP)
        display.clear()

    def choose_players(self):
        """
        Routine to choose the players.

        The first player to press the A button will be PLAYER_1.
        The second player to press the B button will be PLAYER_2.
        """
        display.show(Image("00990:00900:00900:99999:09990"))

        while True:
            if button_a.is_pressed():
                radio.send("PLAYER_1 READY")
                while True:
                    message = radio.receive()
                    sleep(100)
                    if message and message == "PLAYER_2 READY":
                        self.me.player_number = "PLAYER_1"
                        self.opponent.player_number = "PLAYER_2"
                        display.show("1")
                        break
                break

            if button_b.is_pressed():
                while True:
                    message = radio.receive()
                    sleep(100)
                    if message and message == "PLAYER_1 READY":
                        radio.send("PLAYER_2 READY")
                        self.me.player_number = "PLAYER_2"
                        self.opponent.player_number = "PLAYER_1"
                        display.show("2")
                        break
                break

        sleep(1000)

    def end(self, win):
        """
        Routine to end the game.

        If the player wins, show a happy face.
        If the player loses, show a sad face.
        """
        if win:
            display.show(Image.HAPPY)
            music.play(music.CHASE)
        else:
            display.show(Image.SAD)
            music.play(music.WAWAWAWAA)

    def lost(self):
        """
        Check if the player has lost the game.

        The player loses the game if the opponent hits all the ships.
        """
        for i in range(5):
            for j in range(5):
                if self.sea.board[i][j] == SHIP and self.opponent.shots[i][j] != SHIP:
                    return False
        return True

    def send_shot(self):
        """
        Send a shot to the opponent.

        The player shoots in the opponent's game board.
        The opponent will respond with the result of the shot and if the player has won the game.
        The player will mark the result of the shot in the player board.

        Returns True if the current player has won the game.
        """
        self.me.shoot()

        message = str(self.me.row) + " " + str(self.me.col)
        radio.send(message)

        response = None
        while not response:
            response = radio.receive()
            sleep(100)

        hit, won = response.split(" ")
        hit = hit == "True"
        won = won == "True"

        self.me.mark(self.me.row, self.me.col, hit)

        if hit:
            display.show(Image.TARGET)
            music.play(music.POWER_UP)
        else:
            display.show(Image.NO)
            music.play(music.POWER_DOWN)

        return won

    def receive_shot(self):
        """
        Receive a shot from the opponent.

        The player will receive a shot from the opponent.
        The player will mark the result of the shot in the opponent board.
        The player will respond with the result of the shot and if the opponent has won the game.

        Returns True if the current player has lost the game.
        """
        self.sea.show()

        response = None
        while not response:
            response = radio.receive()
            sleep(100)

        row, col = response.split(" ")
        row = int(row)
        col = int(col)

        self.sea.blink(row, col)
        hit = self.sea.hit(row, col)
        self.opponent.mark(row, col, hit)

        lost = self.lost()

        message = str(hit) + " " + str(lost)
        radio.send(message)

        if hit:
            display.show(Image.TARGET)
            music.play(music.POWER_DOWN)
        else:
            display.show(Image.NO)
            music.play(music.POWER_UP)

        return lost

    def run(self):
        """
        Run the logic of the game.

        Player 1 starts the game by sending a shot and receiving a shot from Player 2.
        Player 2 sends a shot and receives a shot from Player 1.

        The game ends when a player wins.

        The player wins by hitting all the opponent's ships before the opponent.
        """
        self.start()
        self.choose_players()

        while True:
            if self.me.player_number == "PLAYER_1":
                if self.send_shot():
                    self.winner = self.me.player_number
                    break
                if self.receive_shot():
                    self.winner = self.opponent.player_number
                    break
            elif self.me.player_number == "PLAYER_2":
                if self.receive_shot():
                    self.winner = self.opponent.player_number
                    break
                if self.send_shot():
                    self.winner = self.me.player_number
                    break

        self.end(self.winner == self.me.player_number)


game = Game()
game.run()
