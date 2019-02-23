"""
Simple CLI Tic Tac Toe game written in python
Author: Adam Keesey

\U0000274c X
\U0001f535 O
"""
import sys
import os


class TicTacToe():
    """ Tic Tac Toe Game Class """

    def __init__(self):
        self.player = ""
        self.player_move = ""
        self.grid = [
            ['  ', '  ', '  '],
            ['  ', '  ', '  '],
            ['  ', '  ', '  '],
        ]
        self.turn = 0
        self.valid_moves = [
            "A1", "A2", "A3",
            "B1", "B2", "B3",
            "C1", "C2", "C3",
        ]
        self.grid_taken = []

    def draw_grid(self):
        """ Draw the game grid """
        os.system("clear")
        print("  A  | B  | C ")
        print("1 {} | {} | {}".format(*self.grid[0]))
        print("2 {} | {} | {}".format(*self.grid[1]))
        print("3 {} | {} | {}".format(*self.grid[2]))

    def get_player_move(self):
        """ Get the players move """

        self.player = "\U0000274c" if self.turn else "\U0001f535"

        self.player_move = input("Where you want to go? ")

        self.player_move = self.player_move.upper()

        if self.player_move not in self.valid_moves:
            print("Not a valid move")
            self.get_player_move()

        letter = self.player_move[0]
        number = self.player_move[1]

        self.store_player_move(letter, number)

    def store_player_move(self, letter, number):
        """
        Store players move and check to see if they won and
        if moves are left
        """

        if letter == "A":
            index = 0
        elif letter == "B":
            index = 1
        else:
            index = 2

        if letter + number in self.grid_taken:
            print("Move already taken try again")
            self.get_player_move()

        self.grid[int(number) - 1][index] = self.player
        self.grid_taken.append(letter + number)

        self.turn = not self.turn  # Change turn
        self.draw_grid()

        if self.won():
            print("Player {} wins!".format(self.player))
            sys.exit()

        if not self.moves_left():
            print("No winner, try again!")
            sys.exit()

        self.get_player_move()

    def won(self):
        """ Check to see if the current player has won"""
        won = False

        winning_combos = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
        ]

        for combos in winning_combos:
            win_check = [False, False, False]
            for i, _ in enumerate(combos):
                number, index = combos[i]
                if self.grid[number][index] == self.player:
                    win_check[i] = True

            if False not in win_check:
                won = True

        return won

    def moves_left(self):
        """ Check to see if there any moves left to take """
        moves = False

        for row in self.grid:
            if "  " in row:
                moves = True

        return moves


def main():
    """ Main program function """
    game = TicTacToe()
    game.draw_grid()
    game.get_player_move()


if __name__ == "__main__":
    main()
