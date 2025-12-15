import unittest
import chess

class TestSanity(unittest.TestCase):
    def test_start_position_has_legal_moves(self):
        board = chess.Board()
        self.assertGreater(len(list(board.legal_moves)), 0)

if __name__ == "__main__":
    unittest.main()
