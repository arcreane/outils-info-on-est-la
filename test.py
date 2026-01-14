import unittest

from Player import Player


class TestStringMethods(unittest.TestCase):

    def test_set_pos(self):
        player = Player(720, 300)
        player.set_position(0, 500)

if __name__ == '__main__':
    unittest.main()