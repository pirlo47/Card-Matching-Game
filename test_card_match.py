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
    
    #Test for selecting cards 
    def setup(self):
        #initialize a deck and match testing for two cards 
        self.deck = board_grid()
        self.matched_positions = {0, 2} #Assume cards at position  zero and 2 are matched 

    #test for valid selection  
    def test_for_valid_selection(self):
        result = select_card(self.deck , 1, 3, self.matched_position)
        self.assertIsInstance(result, tuple, "Valid selection should return a tuple of two cards")
        self.assertEqual(len(result), 2, "Two cards should be returned for a valid selection")
        
       


if __name__ == "__main__":
    unittest.main()