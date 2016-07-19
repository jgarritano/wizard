import unittest
from game import Player

class GameTest(unittest.TestCase):
    def test_gold_of_a_new_player_should_be_None(self):
        myPlayer = Player()
        self.assertIsNone(myPlayer.gold)

    def test_setInt(self):
        myPlayer = Player()
        myPlayer.setInt(4)
        self.assertEqual(myPlayer.myInt,4)
    
