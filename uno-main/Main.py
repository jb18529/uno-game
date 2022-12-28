import pygame
from pygame.locals import *
import graphics.graphics
import card_logic
import playing_classes_graphics
import AI_logic
import Gameover_Screen
import Game_start_screen
import background_choice

#import all the files you need:
max_display_size_x=1200
max_display_size_y=620
card_width=80
card_height=127 

def drawing_card_action(draw_pile, players_dict, p_num):    
    #use draw_pile to get drawpile list of card objects
    draw_card = draw_pile[0]
    draw_pile.pop(0)
    players_dict[p_num].append(draw_card)

def any_cards_playable(players_dict, p_num, discard_pile):
    playable_card = []
    if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
      for p_card in players_dict[p_num]:
        if p_card.colour == discard_pile.list_of_discard[-1].colour_choice:
          playable_card.append(p_card)
      return playable_card
    else:
      for p_card in players_dict[p_num]:
        if p_card.colour == discard_pile.list_of_discard[-1].colour or p_card.rank == discard_pile.list_of_discard[-1].rank or p_card.rank=="Wild_draw_four" or p_card.rank=="Wild":
          playable_card.append(p_card)
      return playable_card

def choose_colour_graphics(screen,choose_colour_group, chosen_background):
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # create a text surface object, on which text is drawn on it.
    text = font.render('Choose your Color', True, pygame.Color('green'), pygame.Color('black'))
    
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (550, 200)

    screen.fill(pygame.Color('white'))
    screen.blit(chosen_background.image, chosen_background.rect) 
    screen.blit(text,textRect)
    choose_colour_group.draw(screen)


def update_screen_graphics(player_int,buttons_group,color_display_block_group,drawpiletop_group,screen,graphics_display,players_dict,ai_cards_list,ai_card_length_list,discard_pile, chosen_background):
    #Initialize what the hand for the user cards are and their size and position on the screen
    card_list_group= graphics_display.player_hand_size(players_dict[0],card_width,max_display_size_x,max_display_size_y)
    #Initialize hand for ai player 1 as well as size, position on screen
    ai_position_dict={1:[graphics_display.ai_hand_top], 2:[graphics_display.ai_hand_left,graphics_display.ai_hand_right], 3:[graphics_display.ai_hand_left,graphics_display.ai_hand_top,graphics_display.ai_hand_right]}

    choosen_graph_funcs=ai_position_dict[len(ai_card_length_list)]

    for x in choosen_graph_funcs:

        graphics_ai=x(ai_cards_list[choosen_graph_funcs.index(x)], ai_card_length_list[choosen_graph_funcs.index(x)],card_width,max_display_size_x,max_display_size_y)
        graphics_ai.draw(screen)

    #Assign last card in discard pile, create gui
    last_card_discard = discard_pile.list_of_discard[-1]
    last_card_discard.rect.center = (450, 220) # discard pile position fixed
    discard_pile_gui = pygame.sprite.Group()
    discard_pile_gui.add(last_card_discard)
    
    if last_card_discard.rank=="Wild_draw_four" or last_card_discard.rank=="Wild":
        color_display_block=graphics.graphics.color_block(last_card_discard.colour_choice, 40, 40)
    else:
        color_display_block=graphics.graphics.color_block(last_card_discard.colour, 40, 40)
    
    color_display_block.rect.center=(575,310)
    color_display_block_group.add(color_display_block)    
    screen.fill(pygame.Color('white'))
    screen.blit(chosen_background.image, chosen_background.rect) 

    #draw drawpile onto screen 
    ai_position_dict={1:[graphics_display.ai_hand_top], 2:[graphics_display.ai_hand_left,graphics_display.ai_hand_right], 3:[graphics_display.ai_hand_left,graphics_display.ai_hand_top,graphics_display.ai_hand_right]}
    choosen_graph_funcs=ai_position_dict[len(ai_card_length_list)]
    
    for x in choosen_graph_funcs:
        graphics_ai=x(ai_cards_list[choosen_graph_funcs.index(x)], ai_card_length_list[choosen_graph_funcs.index(x)],card_width,max_display_size_x,max_display_size_y)
        graphics_ai.draw(screen)
    #draw drawpile onto screen
    drawpiletop_group.draw(screen)
    #draw buttons onto screen
    buttons_group.draw(screen)
    #draw user hand onto the screen
    card_list_group.draw(screen)
    #draw discard pile onto screen
    discard_pile_gui.draw(screen)
    #draw the colour display block onto the screen
    color_display_block_group.draw(screen)
    #draw player number
    font = pygame.font.Font('freesansbold.ttf', 20)
    font2 = pygame.font.Font('freesansbold.ttf', 25)
    player_name = ""
    if player_int == 0:
        player_name = "User"
    elif player_int == 1:
        player_name = "AI Player 1"
    elif player_int == 2:
        player_name = "AI Player 2"
    elif player_int == 3:
        player_name = "AI Player 3"
    text = font.render("Now playing: ", True, pygame.Color('white'))#, pygame.Color('black'))
    text2 = font2.render(str(player_name), True, pygame.Color('red'))#, pygame.Color('white'))
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (max_display_size_x-230, 50)
    textRect2.center = (max_display_size_x-100, 50)
    screen.blit(text,textRect)
    screen.blit(text2,textRect2)

def user_wild_wait_colour(clicked_card, chosen_background):
    #Will show screen for colour choice when user picks a wild card 
    screen2 = pygame.display.set_mode((max_display_size_x, max_display_size_y))
    choose_colour_group=pygame.sprite.Group()
    red_button=graphics.graphics.color_block("red", 40, 40)
    red_button.rect.center=(475,310)
    choose_colour_group.add(red_button)   
    blue_button=graphics.graphics.color_block("blue", 40, 40)
    blue_button.rect.center=(525,310)
    choose_colour_group.add(blue_button)   
    green_button=graphics.graphics.color_block("green", 40, 40)
    green_button.rect.center=(575,310)
    choose_colour_group.add(green_button)   
    yellow_button=graphics.graphics.color_block("yellow", 40, 40)
    yellow_button.rect.center=(625,310)
    choose_colour_group.add(yellow_button)   
    color_block_dict2={"red_button":red_button,"blue_button":blue_button,"green_button":green_button,"yellow_button":yellow_button}
    
    flag=0
    running = True
    while True:
    #background
        choose_colour_graphics(screen2,choose_colour_group, chosen_background) 
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            if event.type == MOUSEBUTTONDOWN: 
                if color_block_dict2["red_button"].rect.collidepoint(pygame.mouse.get_pos()):
                    clicked_card.colour_choice = "red"
                    flag=1
                    break
                elif color_block_dict2["green_button"].rect.collidepoint(pygame.mouse.get_pos()):
                    clicked_card.colour_choice = "green"
                    flag=1
                    break
                elif color_block_dict2["blue_button"].rect.collidepoint(pygame.mouse.get_pos()):
                    clicked_card.colour_choice = "blue"
                    flag=1
                    break
                elif color_block_dict2["yellow_button"].rect.collidepoint(pygame.mouse.get_pos()):
                    clicked_card.colour_choice = "yellow" 
                    flag=1
                    break
        if flag==1:
            break
    return clicked_card
        
def user_task_function(draw2_card,draw4_card,skip_card,draw_pile,drawpiletop,pass_button,buttons_group,drawpiletop_group,screen,graphics_display,players_dict,ai_cards_list,ai_card_length_list,discard_pile,color_display_block_group,player_int, chosen_background):#, number_clicked_drawpile = 0):
    #This function allows users to perform actions in the game and is executed when user's turn
    number_clicked_drawpile= 0
    add_rule = 0 
    if skip_card:
        return 0,0,0,0
    if draw2_card:
        for i in range(2):
            drawing_card_action(draw_pile, players_dict, 0)
        return 0,0,0,0
    if draw4_card:
        for i in range(4):
            drawing_card_action(draw_pile, players_dict, 0)
        return 0,0,0,0
    running = True
    while running:
        update_screen_graphics(player_int,buttons_group,color_display_block_group,drawpiletop_group,screen,graphics_display,players_dict,ai_cards_list,ai_card_length_list,discard_pile, chosen_background)
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_q]:
                running = False
                break
            if event.type == MOUSEBUTTONDOWN and add_rule == 0:
                rule_card_list = [] 
                for card in players_dict[0]:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        rule_card_list.append(card)
                if rule_card_list:
                    rule_card = rule_card_list[0]
                    for card in rule_card_list:
                        if int(card.rect[0]>int(rule_card.rect[0])):
                            rule_card = card

                    index_on_playerHand = players_dict[0].index(rule_card)
                    chosen_card = players_dict[0][index_on_playerHand]
                    players_dict[0].pop(index_on_playerHand)
                    discard_pile.bottom_card(chosen_card)
                    drawing_card_action(draw_pile, players_dict, 0)
                    add_rule += 1

            elif event.type == MOUSEBUTTONDOWN and add_rule != 0:
                card_clicked_list=[]
                for card in players_dict[0]:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card_clicked_list.append(card)
                if card_clicked_list:
                    clicked_card=card_clicked_list[0]
                    for card in card_clicked_list:
                        if int(card.rect[0]>int(clicked_card.rect[0])):
                            clicked_card=card
                    if discard_pile.list_of_discard[-1].rank == "Wild" or discard_pile.list_of_discard[-1].rank == "Wild_draw_four":
                        if clicked_card.colour == discard_pile.list_of_discard[-1].colour_choice:
                            index_on_playerHand = players_dict[0].index(clicked_card)
                            chosen_card = players_dict[0][index_on_playerHand]
                            players_dict[0].pop(index_on_playerHand)
                            discard_pile.play_card(chosen_card)
                            if clicked_card.rank == "Skip":
                                return 0,0,1,0
                            elif clicked_card.rank == "Reverse":
                                return 0,0,0,1
                            elif clicked_card.rank == "Draw_two":
                                return 1,0,0,0
                            else:
                                return 0,0,0,0

                    elif clicked_card.colour == discard_pile.list_of_discard[-1].colour or clicked_card.rank == discard_pile.list_of_discard[-1].rank or clicked_card.rank=="Wild_draw_four" or clicked_card.rank=="Wild":
                        if clicked_card.rank == "Wild":
                            clicked_card=user_wild_wait_colour(clicked_card, chosen_background)
                            #index number of selected card
                            index_on_playerHand = players_dict[0].index(clicked_card) 
                            #will be the card object that the user selected 
                            chosen_card = players_dict[0][index_on_playerHand] 
                            #delete card from player hand in dictionary
                            players_dict[0].pop(index_on_playerHand) 
                            #add card to discard pile
                            discard_pile.play_card(chosen_card)
                            return 0,0,0,0
                        elif clicked_card.rank == "Wild_draw_four":
                            clicked_card=user_wild_wait_colour(clicked_card, chosen_background)
                            #index number of selected card
                            index_on_playerHand = players_dict[0].index(clicked_card) 
                            #will be the card object that the user selected
                            chosen_card = players_dict[0][index_on_playerHand] 
                            #delete card from player hand in dictionary
                            players_dict[0].pop(index_on_playerHand)
                            #add card to discard pile
                            discard_pile.play_card(chosen_card)
                            return 0,1,0,0
                        else:
                            #delete card from hand and assign card object to chosen_card
                            index_on_playerHand = players_dict[0].index(clicked_card) #index number of selected card
                            chosen_card = players_dict[0][index_on_playerHand] #will be the card that player 0 selected 
                            players_dict[0].pop(index_on_playerHand) #delete card from player hand in dictionary
                            # #add card to discard pile
                            discard_pile.play_card(chosen_card)
                            if clicked_card.rank == "Skip":
                                return 0,0,1,0
                            elif clicked_card.rank == "Reverse":
                                return 0,0,0,1
                            elif clicked_card.rank == "Draw_two":
                                return 1,0,0,0
                            else:
                                return 0,0,0,0
                #allows user to press pass button and go to next player    
                elif pass_button.rect.collidepoint(pygame.mouse.get_pos()) and number_clicked_drawpile == 1:
                    return 0,0,0,0

                # Click Draw pile and add card to your deck
                elif drawpiletop.rect.collidepoint(pygame.mouse.get_pos()) and add_rule != 0:
                    if number_clicked_drawpile == 0:
                        drawing_card_action(draw_pile, players_dict, 0)
                        number_clicked_drawpile += 1
                        playable_cards = any_cards_playable(players_dict, 0, discard_pile)
                        if len(playable_cards) == 0:
                            return 0,0,0,0

        pygame.display.update()
    return 1, 1, 1, 1 #this is for quitting the game
    

def main():
       
    # Initialise pygame and the window
    pygame.init()
    
    #Game start
    pregame = Game_start_screen.Start_Game(max_display_size_x, max_display_size_y)
    num_of_plyrs, background_name = pregame.start_screen()

    #Display window
    screen = pygame.display.set_mode((max_display_size_x, max_display_size_y))
    #background
    chosen_background = background_choice.choosing_background_pic(max_display_size_x, max_display_size_y, background_name)
    screen.fill(pygame.Color('white'))
    screen.blit(chosen_background.image, chosen_background.rect)    
    pygame.display.set_caption('Uno Game')
    
    #Start logic
    start_game=card_logic.preparegame(num_of_plyrs)
    players_dict=start_game.player_dict  
    draw_pile=start_game.decklist 
    #Create instance of class DiscardCard Pile
    discard_pile = playing_classes_graphics.DiscardCard_Pile()

    #Graphics for the draw pile
    drawpiletop=card_logic.Card(card_name="unocardback")
    drawpiletop.rect.center=(700,350)
    drawpiletop_group=pygame.sprite.Group()
    drawpiletop_group.add(drawpiletop)

    #Graphics for the pass button
    pass_button=graphics.graphics.button("pass_button", 40, 40)
    pass_button.rect.center=(425,310)
    
    buttons_group=pygame.sprite.Group()
    buttons_group.add(pass_button)
    
    #creating input variables for ai function graphics
    ai_card_length_list=[]
    ai_cards_list=[]
    for i in range(1,num_of_plyrs):
        ai_card_length_list.append(len(players_dict[i]))
        ai_cards_list.append(players_dict[i])

    #To start game first take top card from draw pile and add to discard pile 
    while True:
        initial_card=draw_pile[0]
        discard_pile.play_card(initial_card) # now list_of_discard has one card
        draw_pile.pop(0) # removing discarded card from drawpile
        if discard_pile.list_of_discard[-1].rank_id < 10:
            break
    
    initial_color_display_block=graphics.graphics.color_block(initial_card.colour, 40, 40)
    initial_color_display_block.rect.center=(575,310)
    color_display_block_group=pygame.sprite.Group()
    color_display_block_group.add(initial_color_display_block)
    
    #Create instance of AI logic class EASY level
    ai_activated_l = {}
    for i in range(1, len(players_dict.keys())):
        ai_activated = AI_logic.Easy_AI()
        ai_activated_l[i] = ai_activated
    #Access correct graphics file in graphics folder
    graphics_display = graphics.graphics

    #Game variables that determine flow of game
    # if rev is False game direction normal (counterclockwise) is True -> (clockwise)
    playerlist=list(players_dict.keys())
    player_int=-1
    rev = False
    playing_skip=0
    playing_rev=0
    playing_draw2=0
    playing_draw4=0
    winner_name = ""
    
    # Main loop of the game - checking for new events and rendering the window picture
    running=True
    while running:
        #pygame.event.pump() to prevent game from crashing when ai's are playing
        pygame.event.pump()
        if rev is False:
            player_int=player_int+1
            if player_int >=len(playerlist):
                player_int=0
        if rev is True:
            player_int=player_int-1
            if player_int <0:
                player_int=len(playerlist)-1
    
        update_screen_graphics(player_int,buttons_group,color_display_block_group,drawpiletop_group,screen,graphics_display,players_dict,ai_cards_list,ai_card_length_list,discard_pile, chosen_background)
        
        for i in range(0, num_of_plyrs):
            if len(players_dict[i]) == 0:
                if i == 0:
                    winner_name = "You"
                else:
                    winner_name = f"AI Player {i}"
                running = False
                break

        if player_int == 0:
            pygame.time.delay(1000)
            playing_draw2,playing_draw4,playing_skip,playing_rev=user_task_function(playing_draw2,playing_draw4,playing_skip,draw_pile,drawpiletop,pass_button,buttons_group,drawpiletop_group,screen,graphics_display,players_dict,ai_cards_list,ai_card_length_list,discard_pile,color_display_block_group,player_int, chosen_background)
            #check status of draw pile and if it is low in number move cards from discard to draw pile
            if len(draw_pile) < 10:
                draw_pile.extend(discard_pile.list_of_discard[:-2])
                del discard_pile.list_of_discard[:-2]
            # this code is if player quits the game returning 1, 1, 1, 1 so all True
            if playing_draw2 == True and playing_draw4 == True and playing_rev == True and playing_rev == True:
                break
            if playing_rev: #if playing_rev == 1
                rev = not rev

        if player_int != 0:
            pygame.time.delay(1000)             
            playing_draw2,playing_draw4,playing_skip,playing_rev=ai_activated_l[player_int].AI_action(playing_draw2,playing_draw4,playing_skip,players_dict[player_int], start_game, discard_pile)
            #check status of draw pile and if it is low in number move cards from discard to draw pile
            if len(draw_pile) < 10:
                draw_pile.extend(discard_pile.list_of_discard[:-2])
                del discard_pile.list_of_discard[:-2]
            if playing_rev:
                rev = not rev
        pygame.display.update()

    #Calculate points at end of game
    points_list = []    
    for end in range(0, num_of_plyrs):
        total_p = 0
        for card_end in players_dict[end]:
            total_p += card_end.point
        points_list.append(total_p)

    endGame = Gameover_Screen.Gameover(max_display_size_x, max_display_size_y)
    if num_of_plyrs == 2:
        endGame.end_game(winner_name,num_of_plyrs, points_list[0], points_list[1])
    elif num_of_plyrs == 3:
        endGame.end_game(winner_name, num_of_plyrs, points_list[0], points_list[1], points_list[2])
    elif num_of_plyrs == 4:
        endGame.end_game(winner_name, num_of_plyrs, points_list[0], points_list[1], points_list[2],points_list[3])

    pygame.quit()

if __name__ == '__main__':
    main()


    
