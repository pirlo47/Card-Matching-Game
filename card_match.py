


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

#create a function that selects two card 
def card_selected (playerInput, deck):
    