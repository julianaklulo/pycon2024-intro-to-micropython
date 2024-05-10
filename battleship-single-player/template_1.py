from microbit import *
import random


SHIP = 9
WATER = 2


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


sea = Sea()
sea.show()
