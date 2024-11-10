import unittest
from card_match import * 


class TestCardMatch(unittest.TestCase):

    #Test for generating an even number of unique cards 
    def test_board_for_16_unique_pairs(self):
        deck = board_grid()
    
        #test that the total number of cards is 32 
        self.assertEqual(len(deck) , 32)

        #test for exactly 16 unique pairs 
        self.assertEqual(len(set(deck)), 16)

        #check that each unique card appears exactly twice 
        for card in set(deck):
            self.assertEqual(deck.count(card), 2)

    def test_card_selection(self):
        deck = board_grid()
        playerInput = 

        #test for selecting two cards 
        self.assertIn(card_selected(deck), playerInput)


if __name__ == "__main__":
    unittest.main()