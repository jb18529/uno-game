import pygame
from pygame.locals import *
import card_logic
 
def player_hand_size(card_list,card_width,max_display_size_x,max_display_size_y):
    card_list_group = pygame.sprite.Group()
    no_of_cards=len(card_list)
    min_x=400 #min_x is the x coordinate
    max_x=(card_width/2)*(no_of_cards+1) #max length of gui player hand
    out_of_screen=False
    if (max_x+400)>max_display_size_x: #if length length of player hand is bigger than screen, readjust the card width
        out_of_screen=True
        max_x=max_display_size_x-300
        card_width=(max_x-min_x)/no_of_cards
    for card in card_list:
        min_x=min_x+(card_width/2)
        if out_of_screen is True:
            min_x=min_x+(card_width/2) #card_width/2 is the spacing between cards
        card.rect.center=(min_x,max_display_size_y-100)
        card_list_group.add(card)
    return card_list_group

def ai_hand_top(card_list, length_card_list, card_width, max_display_size_x, max_display_size_y):
    ai_card_top_group = pygame.sprite.Group()
    min_x = 400
    max_x = (card_width/2)*(length_card_list+1)
    out_of_screen = False
    if (max_x+400) > max_display_size_x:
        out_of_screen = True
        max_x = max_display_size_x - 300
        card_width = (max_x-min_x)/length_card_list
    for card in card_list:
        ai_card_gui = card_logic.Card(card_name="ai_hand")
        min_x = min_x + (card_width/2)
        if out_of_screen is True:
            min_x = min_x + (card_width/2) + 20
        ai_card_gui.rect.center=(min_x,75)
        ai_card_top_group.add(ai_card_gui)
    #flip these cards
    return ai_card_top_group

def ai_hand_right(card_list, length_card_list, card_width, max_display_size_x, max_display_size_y):
    ai_card_right_group = pygame.sprite.Group()
    min_y = 100
    max_y = (card_width/2)*(length_card_list+1)
    out_of_screen = False
    if (max_y+400) > max_display_size_y:
        out_of_screen = True
        max_y = max_display_size_y - 300
        card_width = (max_y-min_y)/length_card_list
    for card in card_list:
        ai_card_gui = card_logic.Card(card_name="ai_handright")
        min_y = min_y + (card_width/2)
        if out_of_screen is True:
            min_y = min_y + (card_width/2)
        ai_card_gui.rect.center=(max_display_size_x - 80,min_y)
        ai_card_right_group.add(ai_card_gui)
    #flip these cards
    return ai_card_right_group

def ai_hand_left(card_list, length_card_list, card_width, max_display_size_x, max_display_size_y):
    ai_card_left_group = pygame.sprite.Group()
    min_y = 100
    max_y = (card_width/2)*(length_card_list+1)
    out_of_screen = False
    if (max_y+400) > max_display_size_y:
        out_of_screen = True
        max_y = max_display_size_y - 300
        card_width = (max_y-min_y)/length_card_list
    for card in card_list:
        ai_card_gui = card_logic.Card(card_name="ai_handleft")
        min_y = min_y + (card_width/2)
        if out_of_screen is True:
            min_y = min_y + (card_width/2)
        ai_card_gui.rect.center=(80,min_y)
        ai_card_left_group.add(ai_card_gui)
    #flip these cards
    return ai_card_left_group

class button(pygame.sprite.Sprite):
    def __init__(self, name, button_width, button_height):
        super().__init__()
        self.name=name
        self.image = pygame.transform.smoothscale(pygame.image.load("uno_cards_image/"+self.name+".jpg"), (button_width, button_height))  
        self.rect = self.image.get_rect()

class color_block(pygame.sprite.Sprite):
    def __init__(self,name,block_width, block_height):
        super().__init__()
        self.name=name
        self.image = pygame.transform.smoothscale(pygame.image.load("uno_cards_image/"+self.name+"-block"+".jpg"), (block_width, block_height))  
        self.rect = self.image.get_rect()

