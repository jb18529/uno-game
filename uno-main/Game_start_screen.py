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

class screenPicture(pygame.sprite.Sprite):
    def __init__(self, path, width = 110, height = 110):
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load(path), (width, height)) 
        self.rect = self.image.get_rect()

class Start_Game():
    def __init__(self, display_x, display_y):
        self.display_x = display_x
        self.display_y = display_y

    def start_screen(self):
        
        background_color = pygame.Color('orange')

        screen = pygame.display.set_mode((self.display_x, self.display_y))
        screen.fill(background_color)

        number1 = screenPicture('1.png')
        number1.rect.center = ((self.display_x)/4, 250)

        number2 = screenPicture('2.png')
        number2.rect.center = (2*((self.display_x)/4), 250)

        number3 = screenPicture('3.png')
        number3.rect.center = (3*((self.display_x)/4), 250)

        desert = screenPicture('background_images_uno/desert.jpg', 200, 150)
        forest = screenPicture('background_images_uno/forest.jpg', 200, 150)
        snow = screenPicture('background_images_uno/snow.jpg', 200, 150)

        desert.rect.center = ((self.display_x)/4, 475)
        forest.rect.center = (2*((self.display_x)/4), 475)
        snow.rect.center = (3*((self.display_x)/4), 475)

        objects = pygame.sprite.Group()
        objects.add(number1)
        objects.add(number2)
        objects.add(number3)

        picObjects = pygame.sprite.Group()
        picObjects.add(desert)
        picObjects.add(forest)
        picObjects.add(snow)
        number_of_players = 0
        background_choice = ""

        pygame.init()
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    running=False
                Welcome_label1 = Label('Welcome to Uno Game',(self.display_x/3.5, 50),80,'white')
                Welcome_label2 = Label('CLICK ON THE NUMBER OF AI PLAYERS YOU WOULD LIKE TO PLAY WITH', (self.display_x/6.8, 140), 35, 'white')
                Welcome_label3 = Label('THEN CLICK ON YOUR CHOICE OF BACKGROUND', (self.display_x/3.8, 360), 35, 'white')
                Welcome_label1.draw(screen)
                Welcome_label2.draw(screen)
                Welcome_label3.draw(screen)
                objects.draw(screen)
                picObjects.draw(screen)

                if event.type == MOUSEBUTTONDOWN:
                    if number1.rect.collidepoint(pygame.mouse.get_pos()):
                        number_of_players = 2
                    elif number2.rect.collidepoint(pygame.mouse.get_pos()):
                        number_of_players = 3
                    elif number3.rect.collidepoint(pygame.mouse.get_pos()):
                        number_of_players = 4
                    elif desert.rect.collidepoint(pygame.mouse.get_pos()):
                        background_choice = "desert"
                    elif forest.rect.collidepoint(pygame.mouse.get_pos()):  
                        background_choice = "forest"                        
                    elif snow.rect.collidepoint(pygame.mouse.get_pos()):  
                        background_choice = "snow"
                if number_of_players != 0 and background_choice != "":
                    print(number_of_players, background_choice)
                    return number_of_players, background_choice
                
            pygame.display.update()

    pygame.quit()
