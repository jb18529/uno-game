import random
import card_logic 
from pygame.locals import *

        
class AI_logic:
  def __init__(self):
      pass
    
class Easy_AI:
  def AI_action(self, draw2_card,draw4_card,skip_card, AI_hand, game_part, discard_pile):
    if skip_card:
      return 0,0,0,0
    if draw2_card:
        for i in range(2):
          draw_cardAI = game_part.decklist
          AI_hand.append(draw_cardAI[0])#draw top card from drawpile and add to ai hand
          draw_cardAI.pop(0)
        return 0,0,0,0
    if draw4_card:
        for i in range(4):
          draw_cardAI = game_part.decklist
          AI_hand.append(draw_cardAI[0])#draw top card from drawpile and add to ai hand
          draw_cardAI.pop(0)
        return 0,0,0,0
    
    # Draw card from drawpile (decklist) and delete card from drawpile
    #Choosing random card from ai hand inserting to bottom of discard pile and removing card from AI hand
    worst_card = random.choice(AI_hand)
    AI_hand.remove(worst_card)
    discard_pile.bottom_card(worst_card)
    AI_hand.append(game_part.decklist[0])
    game_part.decklist.pop(0)
    Chosen_card = self.AI_choose_card(AI_hand, discard_pile)
    wild_colours = ["red", "green", "blue", "yellow"]

    if len(Chosen_card) != 0:
      Best_card = random.choice(Chosen_card)
      if Best_card.rank == "Skip":
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card) #Adding the chosen card to the top of the discard pile - playing your card
        return 0,0,1,0
      elif Best_card.rank == "Reverse":
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card)
        return 0,0,0,1
      elif Best_card.rank == "Draw_two":
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card)
        return 1,0,0,0
      elif Best_card.rank == "Wild":
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card)
        return 0,0,0,0
      elif Best_card.rank == "Wild_draw_four":
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card)
        return 0,1,0,0
      else:
        AI_hand.remove(Best_card) #removed the chosen card from hand
        discard_pile.play_card(Best_card) #Adding the chosen card to the top of the discard pile - playing your card
        return 0,0,0,0

    else:
      draw_cardAI = game_part.decklist
      AI_hand.append(draw_cardAI[0])#draw top card from drawpile and add to ai hand
      draw_cardAI.pop(0) #remove top card which is [0] from drawpile 
      Best_Card_List=self.AI_choose_card([AI_hand[-1]], discard_pile)
      if len(Best_Card_List)!=0:
        Best_card=Best_Card_List[0]
        if Best_card.rank == "Skip":
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card) #Adding the chosen card to the top of the discard pile - playing your card
          return 0,0,1,0
        elif Best_card.rank == "Reverse":
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 0,0,0,1
        elif Best_card.rank == "Draw_two":
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 1,0,0,0
        elif Best_card.rank == "Wild":
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 0,0,0,0
        elif Best_card.rank == "Wild_draw_four":
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 0,1,0,0
        else:
          AI_hand.remove(Best_card) #removed the chosen card from hand
          discard_pile.play_card(Best_card) #Adding the chosen card to the top of the discard pile - playing your card
          return 0,0,0,0
      else:
        return 0,0,0,0

  def AI_choose_card(self, AI_hand, discard_pile):
    Correct_cards = []
    #if card on discard pile is already a wild or wild draw four then ai has to match the correct colour from colour_choice
    if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour_choice:
          Correct_cards.append(card)
      return Correct_cards
    else:
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour or card.rank == discard_pile.list_of_discard[-1].rank or \
                card.rank=="Wild_draw_four" or card.rank=="Wild":
          Correct_cards.append(card)
      return Correct_cards