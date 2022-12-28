import pygame
from pygame.locals import *
import random

class Card(pygame.sprite.Sprite):
    def __init__(self, colour_id = 0, rank_id = 0, card_name="", card_width=80, card_height=127): #colour_id, rank_id
        super().__init__()
        self.rank_id = rank_id
        self.colour_id = colour_id
        if self.rank_id == 10:
            self.rank = "Skip"
            self.point = 20
        elif self.rank_id == 11:
            self.rank = "Draw_two"
            self.point = 20
        elif self.rank_id == 12:
            self.rank = "Reverse"
            self.point = 20
        #numbered cards
        if 0 <= self.rank_id <= 9:
            self.rank = self.rank_id
            self.point = self.rank_id
        if self.colour_id == 0:
            self.colour = "red"
        elif self.colour_id == 1:
            self.colour = "green"
        elif self.colour_id == 2:
            self.colour = "blue"
        elif self.colour_id == 3:
            self.colour = "yellow"
        elif self.colour_id==4: #wild
            self.colour="black"
            self.rank_id = 13
            self.rank = "Wild"
            self.point = 50
            self.colour_choice = "rainbow" 
        elif self.colour_id==5: # wild draw card
            self.colour="black"
            self.rank_id = 14
            self.rank = "Wild_draw_four"
            self.point = 50
            self.colour_choice = "rainbow"
        if card_name=="":
            self.name=str(self.colour.lower())+str(self.rank_id)
        else:
            self.name=card_name
        if self.name == "ai_handleft" or self.name == "ai_handright":
            self.image = pygame.transform.smoothscale(pygame.image.load("uno_cards_image/uno_card-"+self.name+".jpg"), (card_height, card_width))
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.transform.smoothscale(pygame.image.load("uno_cards_image/uno_card-"+self.name+".jpg"), (card_width, card_height)) 
            self.rect = self.image.get_rect()
    def __repr__(self):
        return str(self.colour) + " " + str(self.rank) + " Points:" + str(self.point)

class preparegame():
    def __init__(self,no_of_players = 2):
        self.decklist=[]
        self.player_dict = {}
        self.no_of_players=no_of_players
        self.create_deck()
        self.prepare_cards()

    def create_deck(self):
        for colour_id in range(0, 6):
            # adding 4 wild cards 
            if colour_id == 4:
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))
            #adding 4 wild draw cards
            elif colour_id == 5:
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))
                self.decklist.append(Card(colour_id, rank))

            if colour_id < 4:
                for rank in range(0, 10): 
                    if rank==0:
                        self.decklist.append(Card(colour_id, rank))
                    if 1<=rank<=12:
                        self.decklist.append(Card(colour_id, rank))
                        self.decklist.append(Card(colour_id, rank))

                for rank in range(10, 13):
                    self.decklist.append(Card(colour_id, rank))
                    self.decklist.append(Card(colour_id, rank))

    def prepare_cards(self):
 
        for player in range(0, self.no_of_players):
            hand = []
            for i in range(0, 7):
                a = random.choice(self.decklist)
                hand.append(a)
                self.decklist.remove(a)
            #append hand list of cards to players list to form a list of all players hands
            self.player_dict[player]=hand
        random.shuffle(self.decklist)
        # after deck initilisation, you get dictionary of players and cards + drawpile 


