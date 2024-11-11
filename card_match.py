


#create a board grid of cards placed faced down 

def board_grid ():
    #create an empty deck 
    deck = []

    #create cards with values corresponding to their suit 
    values = ["A","2", "3", "4", "5", "6", "7", "8"]
    suits = ["Heart", "Spade"]

    #generate unique cards 
    unique_cards = []
    for suit in suits:
        for value in values: 
            cardValue = f"{value} {suit}"
            unique_cards.append(cardValue)
            
    deck = unique_cards * 2  #duplicate each cards to get 32 cards 
                
    return deck 

#create a function that selects two cards and validates them 
def select_card(deck, pos1 , pos2, matched_position):
    #Check if positions are within bounds 
    if pos1 < 0 or pos2 < 0 or pos1 >= len(deck) or pos2 >= len(deck):
        return "Invalid selection: Out of bounds"
    #check if positions are the same 
    if pos1 == pos2: 
        return "Invalid: Same card selected"
    
    #check if cards are already matched 
    if pos1 in matched_position or pos2 in matched_position:
        return "Invalid Card already Matched"
    #return valid selection 
    return (deck[pos1], deck[pos2])
    
    
    