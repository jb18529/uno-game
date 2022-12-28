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
                  #\
                #or card.rank_id == 13 or card.rank_id ==14:
          Correct_cards.append(card)
      return Correct_cards

class Common_AI:
  def AI_action(self, draw2_card, draw4_card, skip_card, AI_hand, game_part, discard_pile):
    if skip_card:
      print("skipping AI")
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour)
      return 0, 0, 0, 0
    if draw2_card:
      print("draw2 AI")
      for i in range(2):
        draw_cardAI = game_part.decklist
        # print(draw_cardAI[0])
        AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
        # print(AI_hand)
        draw_cardAI.pop(0)
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour)
      return 0, 0, 0, 0
    if draw4_card:
      print("draw4 AI")
      for i in range(4):
        draw_cardAI = game_part.decklist
        # print(draw_cardAI[0])
        AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
        # print(AI_hand)
        draw_cardAI.pop(0)
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour_choice)
      return 0, 0, 0, 0
    # Correct_card = []
    # Bad_card = AI_hand
    # Extra Rule
    # Worst_card = random.choice(Bad_card)
    # AI_hand.list.remove(Worst_card)

    # Draw card from drawpile (decklist) and delete card from drawpile

    # Choosing random card from ai hand inserting to bottom of discard pile and removing card from AI hand
    # print("------------------------")

    #Choose worst card
    Bad_card = []
    for card in AI_hand:
      if card.colour != discard_pile.list_of_discard[-1].colour and card.rank != discard_pile.list_of_discard[-1].rank \
              and card.rank != "Wild_draw_four" and card.rank != "Wild":
        Bad_card.append(card)
    if Bad_card != []:
      Worst_card = random.choice(Bad_card)
    else:
      Worst_card = random.choice(AI_hand)

    #card_add_rule = random.choice(AI_hand)
    # print("Card_add_rule:",card_add_rule)
    AI_hand.remove(Worst_card)
    # print(discard_pile.list_of_discard[0])
    discard_pile.bottom_card(Worst_card)
    # print("discard pile:", discard_pile.list_of_discard[0])
    # drawing card from drawpile and adding to AI hand
    # print("AI hand before:", AI_hand)
    AI_hand.append(game_part.decklist[0])
    # print("AI hand after:", AI_hand)
    # print("draw pile before:", game_part.decklist[0])
    game_part.decklist.pop(0)
    # print("draw pile after:", game_part.decklist[0])
    # print("----------------------")

    #Choose best card
    Chosen_card = self.AI_choose_card(AI_hand, discard_pile)
    Special_card = []
    for card in Chosen_card:
      if 10 <= card.rank_id <= 14:
        Special_card.append(card)

    player_hand_list = card_logic.preparegame(2).player_dict[0]

    # for card in AI_hand:
    #     if card.colour == discard_pile.list_of_discard[-1].colour or card.rank == discard_pile.list_of_discard[-1].rank:
    #             #\
    #           #or card.rank_id == 13 or card.rank_id ==14:
    #         Correct_card.append(card)
    wild_colours = ["red", "green", "blue", "yellow"]

    if len(Chosen_card) != 0:
      if len(player_hand_list) <= 3 and Special_card != []:
        Best_card = random.choice(Special_card)
      else:
        Best_card = random.choice(Chosen_card)

      if Best_card.rank == "Skip":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
        print(discard_pile.list_of_discard[-1].name)
        print(Best_card.rank_id)
        print("ai skip")
        return 0, 0, 1, 0
      elif Best_card.rank == "Reverse":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        print("ai reverse")
        return 0, 0, 0, 1
      elif Best_card.rank == "Draw_two":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        return 1, 0, 0, 0
      elif Best_card.rank == "Wild":
        print(" ai wild")
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        return 0, 0, 0, 0
      elif Best_card.rank == "Wild_draw_four":
        print("ai draw 4")
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        return 0, 1, 0, 0
      else:
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
        print(discard_pile.list_of_discard[-1].name)
        return 0, 0, 0, 0

      # playing_classes_graphics.DiscardCard_Pile.play_card(Best_card)
      # Round.Turn += 1
    # Draw card from draw pile and add to hand
    else:
      draw_cardAI = game_part.decklist
      # print(draw_cardAI[0])
      AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
      # print(AI_hand)
      draw_cardAI.pop(0)  # remove top card which is [0] from drawpile
      Best_Card_List = self.AI_choose_card([AI_hand[-1]], discard_pile)
      print("BestCard in else:")
      print(Best_Card_List)
      if len(Best_Card_List) != 0:
        Best_card = Best_Card_List[0]
        # can newly drawn card be play, if so play it
        # if AI_hand[-1] == discard_pile.list_of_discard[-1].colour or AI_hand[-1] == discard_pile.list_of_discard[-1].rank or AI_hand[-1].rank=="Wild_draw_four" or AI_hand[-1].rank=="Wild":
        if Best_card.rank == "Skip":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
          # print(discard_pile.list_of_discard[-1].name)
          print("ai skip")
          return 0, 0, 1, 0
        elif Best_card.rank == "Reverse":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          print("ai reverse")
          return 0, 0, 0, 1
        elif Best_card.rank == "Draw_two":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          return 1, 0, 0, 0
        elif Best_card.rank == "Wild":
          print(" ai wild")
          print(Best_card.rank_id)
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          return 0, 0, 0, 0
        elif Best_card.rank == "Wild_draw_four":
          print("ai draw 4")
          print(Best_card.rank_id)
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 0, 1, 0, 0
        else:
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
          print(discard_pile.list_of_discard[-1].name)
          return 0, 0, 0, 0
      else:
        print("AI passed")
        return 0, 0, 0, 0

  def AI_choose_card(self, AI_hand, discard_pile):
    Correct_cards = []
    # if card on discard pile is already a wild or wild draw four then ai has to match the correct colour from colour_choice
    if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour_choice:
          Correct_cards.append(card)
      return Correct_cards
    else:
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour or card.rank == discard_pile.list_of_discard[-1].rank or \
                card.rank == "Wild_draw_four" or card.rank == "Wild":
          # or card.rank_id == 13 or card.rank_id ==14:
          Correct_cards.append(card)
      return Correct_cards


class Difficult_AI:
  def AI_action(self, draw2_card, draw4_card, skip_card, AI_hand, game_part, discard_pile):
    if skip_card:
      print("skipping AI")
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour)
      return 0, 0, 0, 0
    if draw2_card:
      print("draw2 AI")
      for i in range(2):
        draw_cardAI = game_part.decklist
        # print(draw_cardAI[0])
        AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
        # print(AI_hand)
        draw_cardAI.pop(0)
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour)
      return 0, 0, 0, 0
    if draw4_card:
      print("draw4 AI")
      for i in range(4):
        draw_cardAI = game_part.decklist
        # print(draw_cardAI[0])
        AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
        # print(AI_hand)
        draw_cardAI.pop(0)
      # color_display_block_list.append(discard_pile.list_of_discard[-1].colour_choice)
      return 0, 0, 0, 0
    # Correct_card = []
    # Bad_card = AI_hand
    # Extra Rule
    # Worst_card = random.choice(Bad_card)
    # AI_hand.list.remove(Worst_card)

    # Draw card from drawpile (decklist) and delete card from drawpile

    # Choosing random card from ai hand inserting to bottom of discard pile and removing card from AI hand
    # print("------------------------")

    Colour_match_card = []
    Rank_match_card = []
    Chosen_card = self.AI_choose_card(AI_hand, discard_pile)
    Bad_card = []
    Special_card = []
    for card in Chosen_card:
      if 10 <= card.rank_id <= 14:
        Special_card.append(card)
      if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
          if card.colour == discard_pile.list_of_discard[-1].colour_choice:
            Colour_match_card.append(card)
      else:
          if card.colour == discard_pile.list_of_discard[-1].colour:
            Colour_match_card.append(card)
          if card.rank_id == discard_pile.list_of_discard[-1].rank_id:
            Rank_match_card.append(card)

    #Choose worst card
    for card in AI_hand:
      if card not in Chosen_card:
        Bad_card.append(card)
      if card.colour_id == discard_pile.list_of_discard[-1].colour_id:
        Colour_match_card.append(card)
      if card.rank_id == discard_pile.list_of_discard[-1].rank_id:
        Rank_match_card.append(card)

    if Bad_card != []:
      Worst_card = random.choice(Bad_card)
    elif Rank_match_card != []:
      Worst_card = random.choice(Rank_match_card)
    elif Colour_match_card != []:
      Worst_card = random.choice(Colour_match_card)
    else:
      Worst_card = random.choice(AI_hand)

    #card_add_rule = random.choice(AI_hand)
    # print("Card_add_rule:",card_add_rule)
    AI_hand.remove(Worst_card)
    # print(discard_pile.list_of_discard[0])
    discard_pile.bottom_card(Worst_card)
    # print("discard pile:", discard_pile.list_of_discard[0])
    # drawing card from drawpile and adding to AI hand
    # print("AI hand before:", AI_hand)
    AI_hand.append(game_part.decklist[0])
    # print("AI hand after:", AI_hand)
    # print("draw pile before:", game_part.decklist[0])
    game_part.decklist.pop(0)
    # print("draw pile after:", game_part.decklist[0])
    # print("----------------------")

    #Choose best card
    player_hand_list = card_logic.preparegame(2).player_dict[0]

    # for card in AI_hand:
    #     if card.colour == discard_pile.list_of_discard[-1].colour or card.rank == discard_pile.list_of_discard[-1].rank:
    #             #\
    #           #or card.rank_id == 13 or card.rank_id ==14:
    #         Correct_card.append(card)
    wild_colours = ["red", "green", "blue", "yellow"]

    if len(Chosen_card) != 0:
      # Choose best card
      if len(player_hand_list) > 3:
        if Rank_match_card != []:
          Best_card = random.choice(Rank_match_card)
        elif Colour_match_card != []:
          Best_card = random.choice(Colour_match_card)
        elif Special_card != []:
          Best_card = random.choice(Special_card)
        elif Chosen_card !=[]:
          Best_card = random.choice(Chosen_card)
      else:
        if Special_card != []:
          Best_card = random.choice(Special_card)
        elif Rank_match_card != []:
          Best_card = random.choice(Rank_match_card)
        elif Colour_match_card != []:
          Best_card = random.choice(Colour_match_card)
        elif Chosen_card != []:
          Best_card = random.choice(Chosen_card)

      #remove card from ai hand
      if Best_card.rank == "Skip":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
        print(discard_pile.list_of_discard[-1].name)
        print(Best_card.rank_id)
        print("ai skip")
        return 0, 0, 1, 0
      elif Best_card.rank == "Reverse":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        print("ai reverse")
        return 0, 0, 0, 1
      elif Best_card.rank == "Draw_two":
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        return 1, 0, 0, 0
      elif Best_card.rank == "Wild":
        print(" ai wild")
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)
        return 0, 0, 0, 0
      elif Best_card.rank == "Wild_draw_four":
        print("ai draw 4")
        ai_colour_choice = random.choice(wild_colours)
        Best_card.colour_choice = ai_colour_choice
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        discard_pile.play_card(Best_card)
        print(Best_card.rank_id)
        return 0, 1, 0, 0
      else:
        AI_hand.remove(Best_card)  # removed the chosen card from hand
        print(Best_card.rank_id)
        # Drop_pile.list.insert(0,Best_card)
        discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
        print(discard_pile.list_of_discard[-1].name)
        return 0, 0, 0, 0

      # playing_classes_graphics.DiscardCard_Pile.play_card(Best_card)
      # Round.Turn += 1
    # Draw card from draw pile and add to hand
    else:
      draw_cardAI = game_part.decklist
      # print(draw_cardAI[0])
      AI_hand.append(draw_cardAI[0])  # draw top card from drawpile and add to ai hand
      # print(AI_hand)
      draw_cardAI.pop(0)  # remove top card which is [0] from drawpile
      Best_Card_List = self.AI_choose_card([AI_hand[-1]], discard_pile)
      print("BestCard in else:")
      print(Best_Card_List)
      if len(Best_Card_List) != 0:
        Best_card = Best_Card_List[0]
        # can newly drawn card be play, if so play it
        # if AI_hand[-1] == discard_pile.list_of_discard[-1].colour or AI_hand[-1] == discard_pile.list_of_discard[-1].rank or AI_hand[-1].rank=="Wild_draw_four" or AI_hand[-1].rank=="Wild":
        if Best_card.rank == "Skip":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
          # print(discard_pile.list_of_discard[-1].name)
          print("ai skip")
          return 0, 0, 1, 0
        elif Best_card.rank == "Reverse":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          print("ai reverse")
          return 0, 0, 0, 1
        elif Best_card.rank == "Draw_two":
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          return 1, 0, 0, 0
        elif Best_card.rank == "Wild":
          print(" ai wild")
          print(Best_card.rank_id)
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)
          return 0, 0, 0, 0
        elif Best_card.rank == "Wild_draw_four":
          print("ai draw 4")
          print(Best_card.rank_id)
          ai_colour_choice = random.choice(wild_colours)
          Best_card.colour_choice = ai_colour_choice
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          discard_pile.play_card(Best_card)
          return 0, 1, 0, 0
        else:
          print(Best_card.rank_id)
          AI_hand.remove(Best_card)  # removed the chosen card from hand
          # Drop_pile.list.insert(0,Best_card)
          discard_pile.play_card(Best_card)  # Adding the chosen card to the top of the discard pile - playing your card
          print(discard_pile.list_of_discard[-1].name)
          return 0, 0, 0, 0
      else:
        print("AI passed")
        return 0, 0, 0, 0

  def AI_choose_card(self, AI_hand, discard_pile):
    Correct_cards = []
    # if card on discard pile is already a wild or wild draw four then ai has to match the correct colour from colour_choice
    if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour_choice:
          Correct_cards.append(card)
      return Correct_cards
    else:
      for card in AI_hand:
        if card.colour == discard_pile.list_of_discard[-1].colour or card.rank == discard_pile.list_of_discard[-1].rank or \
                card.rank == "Wild_draw_four" or card.rank == "Wild":
          # \
          # or card.rank_id == 13 or card.rank_id ==14:
          Correct_cards.append(card)
      return Correct_cards
      


















    
