import pygame
from pygame.locals import *

class Label:
    def __init__(self,text,pos,size,colour):
        self.text=text
        self.pos=pos
        self.font = pygame.font.SysFont(None, size)
        self.font_colour = pygame.Color(colour)
    def draw(self,screen):
        img=self.font.render(self.text,True,self.font_colour)
        screen.blit(img,self.pos)

class Gameover:
    def __init__(self, display_x = 1300, display_y = 600, background_color = pygame.Color('red')):
        self.max_display_size_x = display_x
        self.max_display_size_y = display_y
        self.background_color = background_color

    def end_game(self, winner, num_players, user_points, ai1_points, ai2_points = 0, ai3_points = 0): #input: points
        screen = pygame.display.set_mode((self.max_display_size_x, self.max_display_size_y))
        screen.fill(self.background_color)

        pygame.init()
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    running=False
            Game_over_label=Label('GAME OVER!',(self.max_display_size_x/4.5,50),150,'white')

            current_points_label = Label(f'Your points: {user_points}', (self.max_display_size_x/4.5, self.max_display_size_y-340), 36, 'white')
            winner_label=Label(f'Winner in this round: {winner}',(self.max_display_size_x/8, self.max_display_size_y-420), 50, 'white')
            continue_label1=Label('PLAY AGAIN',(self.max_display_size_x/2.3, self.max_display_size_y-100), 40, 'red')
            objects=[]
            if num_players == 2:
                AIplay1_points_label = Label(f'AI Player 1 points: {ai1_points}', (self.max_display_size_x/4.5, self.max_display_size_y-280), 36, 'white')
                objects.append(Game_over_label)
                objects.append(current_points_label)
                objects.append(winner_label)
                objects.append(AIplay1_points_label)
                objects.append(continue_label1)
            elif num_players == 3:
                AIplay1_points_label = Label(f'AI Player 1 points: {ai1_points}', (self.max_display_size_x/4.5, self.max_display_size_y-280), 36, 'white')
                AIplay2_points_label = Label(f'AI Player 2 points: {ai2_points}', (self.max_display_size_x/4.5, self.max_display_size_y-220), 36, 'white')
                objects.append(Game_over_label)
                objects.append(current_points_label)
                objects.append(winner_label)
                objects.append(AIplay1_points_label)
                objects.append(AIplay2_points_label)
                objects.append(continue_label1)
            elif num_players == 4:
                AIplay1_points_label = Label(f'AI Player 1 points: {ai1_points}', (self.max_display_size_x/4.5, self.max_display_size_y-280), 36, 'white')
                AIplay2_points_label = Label(f'AI Player 2 points: {ai2_points}', (self.max_display_size_x/4.5, self.max_display_size_y-220), 36, 'white')
                AIplay3_points_label = Label(f'AI Player 3 points: {ai3_points}', (self.max_display_size_x/4.5, self.max_display_size_y-160), 36, 'white')
                objects.append(Game_over_label)
                objects.append(current_points_label)
                objects.append(winner_label)
                objects.append(AIplay1_points_label)
                objects.append(AIplay2_points_label)
                objects.append(AIplay3_points_label)
                objects.append(continue_label1)

            for obj in objects:
                obj.draw(screen)

            pygame.display.flip()
        pygame.quit()
