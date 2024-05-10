from microbit import *
import random


PLAYER = 7
SHIP = 9
WATER = 2
THRESHOLD = 400


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

    def shoot(self):
        """
        Shoot the board.

        The player can move the cursor with the accelerometer.
        The player can shoot with the A button.

        The coordinates are stored for future reference.
        """
        # WRITE THE LOGIC HERE
        pass

    def mark(self, row, col, hit):
        """
        Mark the player board with the result of the shot.
        """
        if hit:
            self.shots[row][col] = SHIP
        else:
            self.shots[row][col] = WATER

    def show(self):
        """
        Show the player board.
        """
        display.show(
            Image(
                ":".join(["".join(str(point) for point in line) for line in self.shots])
            )
        )

    def blink(self, row, col):
        """
        Blink the given coordinates.

        This is used to show the current coordinates of the player.
        """
        display.set_pixel(col, row, self.shots[row][col])
        sleep(50)
        display.set_pixel(col, row, PLAYER)
        sleep(50)


player = Player()

while True:
    hit = random.choice([True, False])
    player.shoot()
    player.mark(player.row, player.col, hit)
    player.show()
