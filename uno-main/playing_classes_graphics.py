from pygame.locals import *
import card_logic
      
# Players will keep adding one card per turn to the BOTTOM of the discard pile and will choose one card to play on the top of discard pile

class DiscardCard_Pile(card_logic.Card):
    def __init__(self):
      super().__init__()
      self.list_of_discard = []

    def play_card(self, card): # card is an object
      self.list_of_discard.append(card) 

    def bottom_card(self, card):
      self.list_of_discard.insert(0, card)
    


    


        
    
    
        
        
