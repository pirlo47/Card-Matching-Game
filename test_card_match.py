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
    

    #test for valid selection  
    def test_for_valid_selection(self):
        deck = board_grid()
        matched_position= {0, 2}
        
        result = select_card(deck , 1, 3, matched_position)
        self.assertIsInstance(result, tuple, "Valid selection should return a tuple of two cards")
        self.assertEqual(len(result), 2, "Two cards should be returned for a valid selection")
    
    #Test for a selection that is out of bounds
    def test_out_of_bounds(self):
        deck = board_grid()
        matched_positions = {0,2} 
        result = select_card(deck, -1, 3, matched_positions)
        self.assertAlmostEqual(result, "Invalid selection: Out of bounds")
    
    #Test for cards that are the same 
    def test_same_cards(self):
        deck = board_grid()
        matched_positions = {0, 2}
        result = select_card(deck, 1, 1, matched_positions)
        self.assertEqual(result, "Invalid: Same card selected")
    
    #Test for comparing the value of two selected cards 
    def test_for_matching_pair(self):
        deck = board_grid()
        matched_positions = set()

        #assume position 1 and 2 are a matching pair 
        deck[0] = "A Heart"
        deck[1] = "A Heart"

        result = check_for_match(deck, 0, 1, matched_positions)
        self.assertTrue(result, "Matching pair shoukld return True")

        #verify if the cards are in matched_positions
        self.assertIn(0, matched_positions, "Position 0 should be in matched positions")
        self.assertIn(1, matched_positions, "Position 1 should be in matched positions")
    #test for non_matching_pairs 
    def test_non_matching(self):
        deck = board_grid()
        matched_positions = set ()

        deck[0] = "A Heart"
        deck[3] = "4 Spade"

        result =  check_for_match(deck, 0, 3, matched_positions)
        self.assertFalse(result, "Non-matching pair should return False")

        #verify if the cards arre NOT in the matched_positions 
        self.assertNotIn(0, matched_positions, "Position 0 should Not be in matched positions")
        self.assertNotIn(3, matched_positions, "Positions 3 should Not be in matched positions")
    
    #test for game completion 
    def game_completion(self):

        #initialize deck and matched_positions 
        deck = board_grid()
        matched_positions = set ()
        #Initialize matched_positions are all matched cards 
        matched_positions = matched_positions.update(range(len(deck)))
        result = play_game(deck, matched_positions)
        self.assertTrue(result, "All Cards have matching Pairs")
        
    #test for incomplete matches 
    def game_incomplete(self):

        #initialize deck and matched_positions 
        deck = board_grid()
        matched_positions = set ()
        #initialize incomplete matches 
        matched_positions = matched_positions.update([0, 1, 2 ,3])
        result = play_game(deck, matched_positions)

        self.assertFalse(result, "Not all cards match")

if __name__ == "__main__":
    unittest.main()