#!/usr/bin/env python3

class Game:
    alph = (" ", "X", "O")
    """
    A tuple representing the mapping of player marks to symbols.

    alph: tuple
        A tuple where the index corresponds to the player number (0, 1, 2) and the value represents the symbol (empty, X, O).
    """


    def __init__(self, n=3, w=3):
        """
        Initializes a new game instance with the specified board size and winning condition.

        n: int, optional
            The size of the game board (default is 3).
        w: int, optional
            The number of marks in a row required to win (default is 3).
        """
        self.n = n
        self.w = w
        self.player = 0
        self.matrix = [[0 for row in range(n)] for columns in range(n)]


    def __str__(self) -> str:
        """
        Returns a string representation of the game board with borders.

        Returns:
        str:
            A string representing the current state of the game board with borders.
        """
        border = "+---" * self.n + "+\n"
        result = border
        for row in self.matrix:
            result += "| "
            for el in row:
                result += Game.alph[el] + " | "
            result += "\n" + border
        return result


    def make_move(self, row, col):
        """
        Makes a move on the game board at the specified row and column.

        row: int
            The row index of the move.
        col: int
            The column index of the move.
        """
        self.matrix[row][col] = self.player + 1
        self.player = (self.player + 1) % 2

    def get_current_player(self):
        return self.alph[self.player+1]

    def check_draw(self) -> bool:
        for row in self.matrix:
            if 0 in row:
                return False
        return True

    def check_win(self) -> bool:
        """
        Checks whether a winning combination exists on the game board.

        Returns:
        bool:
            True if a winning combination is found, False otherwise.
        """
        for row in range(self.n):
            for col in range(self.n):
                current_player = 2 - self.player
                condition_col = self.n - col >= self.w
                condition_row = self.n - row >= self.w

                if condition_col:
                    # Check row
                    for i in range(self.w):
                        if self.matrix[row][col+i] != current_player:
                            break
                        if i == self.w - 1:
                            return True
                if condition_row:
                    # Check column
                    for i in range(self.w):
                        if self.matrix[row+i][col] != current_player:
                            break
                        if i == self.w - 1:
                            return True
                if condition_col and condition_row:
                    # Check Primary Diagonal
                    for i in range(self.w):
                        if self.matrix[row+i][col+i] != current_player:
                            break
                        if i == self.w - 1:
                            return True
                if col + 1 >= self.w and condition_row:
                    # Check secondary diagonal
                    for i in range(self.w):
                        if self.matrix[row+i][col-i] != current_player:
                            break
                        if i == self.w - 1:
                            return True
        return False


desc = "How to play:\n1) Choose the battlefield size by typing a number from 3 to 5;\n\
* Note: If you choose a battlefield size of 4 or 5, a winning combination will require 4 marks in a row, column, or diagonal.\n\
2) To place a mark in a cell, enter two digits separated by a comma, like this: row, column.\n\
* Note: Row and column indices start from 0. For example, to place a mark in the center of a 3x3 field, enter: 1, 1.\n\
3) After setting up the battlefield, you can type 'r' to restart or 'q' to quit the game.\n\n\
*** Enjoy the game! ***\n\n"


if __name__ == "__main__":
    print(f"\n*** Welcome to TicTacToe! ***\n")
    print(desc)

    
    literal = {"q": "quit", "r": "restart"}

    while True:
        try:
            n = int(input(f"\nChoose battlefield size (3, 4, 5): "))
        except Exception:
            continue
        
        w = 4 if n > 3 else n

        game = Game(n, w)
        print(game)

        while True:
            player = game.get_current_player()
            print(f"\nPlayer '{player}', it's your turn!")
            choose_option = input(f"Choose cell (row, column): ")

            if choose_option in literal.keys():
                YN = input(f"\nAre you sure you want to {literal[choose_option]} the game? (y/n): ")
                if choose_option == "q" and YN.lower() == 'y':
                    print("\nHope to see you later!\n")
                    exit()
                elif choose_option == "r" and YN.lower() == 'y':
                    print("\nLet's try again!\n")
                    break
            
                if YN.lower() == "n":
                    continue

            try:
                row, column = map(int, map(lambda x: x.strip(), choose_option.split(",")))
                if game.matrix[row][column] != 0:
                    print("\nThis cell is already occupied. Choose another one.")
                    continue
                game.make_move(row, column)
                print(game)
            except Exception:
                continue

            if game.check_win():
                print(f"\nCongratulations! Player '{player}' won!")
                break
            elif game.check_draw():
                print("\nThe game ended in a draw!")
                break

        if choose_option == "r":
            continue

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("\nHope to see you later!")
            break

