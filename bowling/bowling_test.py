import unittest
import bowling

class TestBowling(unittest.TestCase):
    def test_gutter_game(self):
        game = bowling.Game()

        game.roll(0)
        game.roll(0)

        game.roll(0)
        game.roll(0)

        self.assertEqual(0, game.score())

if __name__ == '__main__':
    unittest.main()