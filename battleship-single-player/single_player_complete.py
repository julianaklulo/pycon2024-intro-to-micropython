from microbit import *
import music
import random


PLAYER = 7
SHIP = 9
WATER = 2
THRESHOLD = 400


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

        If the coordinates are out of bounds, return False.
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

        The ship must not be near other ships.
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

        The ship will be placed in a random candidate coordinate.
        The orientation can be horizontal or vertical.
        """
        candidates_coordinates = [
            (row, col)
            for row in range(5)
            for col in range(5)
            if self.board[row][col] == WATER
        ]

        while candidates_coordinates:
            row, col = random.choice(candidates_coordinates)
            candidates_coordinates.remove((row, col))

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
        The player can shoot with the A button.

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

        sleep(100)

    def mark(self, row, col, hit):
        """
        Mark the player board with the result of the shot.
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

        The game board is initialized with the ships.
        The player board is initialized.

        The player starts at the top-left corner.
        """
        self.sea = Sea()
        self.player = Player()

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

    def end(self):
        """
        Routine to end the game.
        """
        display.show(Image.HAPPY)
        music.play(music.CHASE)

    def win(self):
        """
        Check if the player has won the game.

        The player wins the game if they hit all the ships.
        """
        for i in range(5):
            for j in range(5):
                if self.sea.board[i][j] == SHIP and self.player.shots[i][j] != SHIP:
                    return False
        return True

    def run(self):
        """
        Run the logic of the game.

        The player can shoot in the board.

        If the player hits a ship, the player board is marked with a ship.
        If the player misses, the player board is marked with water.

        If the player hits all the ships, the game ends.
        """
        self.start()

        while True:
            self.player.shoot()

            hit = self.sea.hit(self.player.row, self.player.col)
            self.player.mark(self.player.row, self.player.col, hit)

            if hit:
                display.show(Image.TARGET)
                music.play(music.POWER_UP)

                if self.win():
                    self.end()
                    break
            else:
                display.show(Image.NO)
                music.play(music.POWER_DOWN)


game = Game()
game.run()
