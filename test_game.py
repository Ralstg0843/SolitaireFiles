
import unittest
from game import SolitaireGame


class TestSolitaireGame(unittest.TestCase):

    def test_new_game(self):
        game = SolitaireGame("english", 7)

        self.assertEqual(game.size, 7)
        self.assertEqual(game.board[3][3], 0)
        self.assertEqual(game.board[2][3], 1)
        self.assertEqual(game.board[0][0], -1)

    def test_valid_move(self):
        game = SolitaireGame("english", 7)

        # Valid move into the empty center
        self.assertTrue(game.is_valid_move(1, 3, 3, 3))

        # Invalid moves
        self.assertFalse(game.is_valid_move(0, 3, 2, 3))
        self.assertFalse(game.is_valid_move(0, 3, 3, 3))
        self.assertFalse(game.is_valid_move(3, 3, 1, 3))

    def test_make_move(self):
        game = SolitaireGame("english", 7)

        result = game.make_move(1, 3, 3, 3)

        self.assertTrue(result)
        self.assertEqual(game.board[1][3], 0)
        self.assertEqual(game.board[2][3], 0)
        self.assertEqual(game.board[3][3], 1)

    def test_game_not_over(self):
        game = SolitaireGame("english", 7)

        self.assertFalse(game.is_game_over())

    def test_game_over(self):
        game = SolitaireGame("english", 7)

        # Clear the board
        for row in range(game.size):
            for col in range(game.size):
                if game.board[row][col] != -1:
                    game.board[row][col] = 0

        # Leave one peg
        game.board[3][3] = 1

        self.assertTrue(game.is_game_over())


if __name__ == "__main__":
    unittest.main()
