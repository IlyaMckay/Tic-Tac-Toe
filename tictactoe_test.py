from tictactoe import Game
import unittest


class Test(unittest.TestCase):
    def test_string(self):
        """
        Description:
            This test case verifies the string representation of an empty game board.

        Expected Outcome:
            The actual string representation of the game board should match the expected string representation, 
            which represents an empty board.
        """
        game = Game()
        actual = str(game)
        expected = "+---+---+---+\n" +\
                   "|   |   |   | \n" +\
                   "+---+---+---+\n" + \
                   "|   |   |   | \n" +\
                   "+---+---+---+\n" +\
                   "|   |   |   | \n" +\
                   "+---+---+---+\n"
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


    def test_check_win_sec_diag(self):
        """
        Description:
            This test case verifies the game's ability to detect a win condition when 
            there are three consecutive marks in the secondary diagonal.

        Expected Outcome:
            The game should detect a win condition when there are three consecutive marks in the secondary diagonal.
        """
        game = Game(4, 3)
        game.make_move(3, 0)  # for X
        game.make_move(2, 0)  # for O
        game.make_move(2, 1)  # for X
        game.make_move(1, 1)  # for O
        game.make_move(1, 2)  # for X
        actual = game.check_win()
        expected = True
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


    def test_check_win_prim_diag(self):
        """
        Description:
            This test case verifies the game's ability to detect a win condition when 
            there are three consecutive marks in the primary diagonal.

        Expected Outcome:
            The game should detect a win condition when there are three consecutive marks in the primary diagonal.
        """
        game = Game(4, 3)
        game.make_move(1, 0)  # for X
        game.make_move(0, 0)  # for O
        game.make_move(2, 0)  # for X
        game.make_move(1, 1)  # for O
        game.make_move(0, 2)  # for X
        game.make_move(2, 2)  # for O
        actual = game.check_win()
        expected = True
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


    def test_check_win_row(self):
        """
        Description:
            This test case verifies the game's ability to detect a win condition 
            when there are three consecutive marks in a row.

        Expected Outcome:
            The game should detect a win condition when there are three consecutive marks in a row.
        """
        game = Game(3, 3)
        game.make_move(0, 0)  # for X
        game.make_move(1, 0)  # for O
        game.make_move(0, 1)  # for X
        game.make_move(1, 1)  # for O
        game.make_move(0, 2)  # for X
        game.make_move(1, 2)  # for O
        actual = game.check_win()
        expected = True
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


    def test_make_move_same_place(self):
        """"
        Description:
            This test case verifies the behavior of the game 
            when a player attempts to make a move in a cell that is already occupied.

        Expected Outcome:
            The game should not detect a win condition
            after a player attempts to make a move in the same cell as a previous move.
        """
        game = Game(4, 3)
        game.make_move(0, 0)  # for X
        game.make_move(0, 0)  # for O
        actual = game.check_win()
        expected = False
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


    def test_check_draw(self):
        """
        Description:
            This test case verifies the behavior of the game 
            when all cells on the game board are occupied, 
            and there is no winner detected.

        Expected Outcome:
            The game should correctly detect that there is no winning combination 
            on the game board, indicating a draw.
        """
        game = Game(5,4)
        game.make_move(0, 0)  # for X
        game.make_move(0, 1)  # for O
        game.make_move(1, 0)  # for X
        game.make_move(1, 1)  # for O
        game.make_move(2, 1)  # for X
        game.make_move(3, 3)  # for O
        game.make_move(4, 2)  # for X
        game.make_move(3, 2)  # for O
        game.make_move(2, 0)  # for X
        game.make_move(3, 0)  # for O
        game.make_move(3, 1)  # for X
        game.make_move(2, 2)  # for O
        game.make_move(4, 0)  # for X
        game.make_move(4, 1)  # for O
        game.make_move(4, 4)  # for X
        game.make_move(4, 3)  # for O
        game.make_move(3, 4)  # for X
        game.make_move(2, 4)  # for O
        game.make_move(2, 3)  # for X
        game.make_move(1, 2)  # for O
        game.make_move(0, 2)  # for X
        game.make_move(1, 3)  # for O
        game.make_move(0, 3)  # for X
        game.make_move(0, 4)  # for O
        game.make_move(1, 4)  # for X
        actual = game.check_win()
        expected = False
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)
        

    def test_actual_expected(self):
        """"
        Description:
            This test case verifies the correctness of the check_win method
            when there is no winning combination on the game board.

        Expected Outcome:
            The actual result returned by the check_win method should match the expected result,
            indicating that there is no winning combination present on the game board.            
        """
        game = Game(4, 4)
        game.make_move(0, 0)  # for X
        game.make_move(0, 1)  # for O
        game.make_move(1, 0)  # for X
        game.make_move(1, 1)  # for O
        game.make_move(2, 0)  # for X
        game.make_move(2, 2)  # for O
        game.make_move(3, 0)  # for X
        game.make_move(2, 3)  # for O
        actual = game.check_win()
        expected = False
        msg = f"Expected == {expected}, Actual == {actual}"
        self.assertEqual(expected, actual, msg)


if __name__ == "__main__":
    unittest.main()
