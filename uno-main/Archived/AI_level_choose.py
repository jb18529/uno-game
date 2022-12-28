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

class Button:
    def __init__(self,pos,path):
        self.pos=pos
        self.path=path
        self.pressed=pygame.image.load(self.path)
        self.unpressed = pygame.image.load(self.path)
        self.size=self.unpressed.get_size()

    def coord_inside_button(self,coord):
        return self.pos[0] <= coord[0] <= self.pos[0]+self.size[0]\
                and self.pos[1] <= coord[1] <= self.pos[1]+self.size[1]

    def draw(self,screen):
        is_pressed= pygame.mouse.get_pressed()[0]\
                    and self.coord_inside_button(pygame.mouse.get_pos())
        screen.blit(self.pressed if is_pressed else self.unpressed, self.pos)

background_color = pygame.Color('black')

max_display_size_x=1466
max_display_size_y=770
screen = pygame.display.set_mode((max_display_size_x, max_display_size_y))
screen.fill(background_color)

pygame.init()
running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    Welcome_label1 = Label('Push the buttons to choose AI player level',(230,100),72,'white')
    Welcome_label2 = Label('Red : easy   Green : normal   Blue : difficult', (355, 250), 55, 'white')

    red_square = Button((350, 450),'red.png')
    green_square = Button((650, 450),'green.png')
    blue_square = Button((950, 450),'blue.png')

    objects = []
    objects.append(Welcome_label1)
    objects.append(Welcome_label2)
    objects.append(red_square)
    objects.append(green_square)
    objects.append(blue_square)



    for obj in objects:
        obj.draw(screen)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 350 <= mouse_x <= 500 and 450 <= mouse_y <= 650:
            print('red')
        elif 650 <= mouse_x <= 850 and 450 <= mouse_y <= 650:
            print('green')
        elif 950 <= mouse_x <= 1150 and 450 <= mouse_y <= 650:
            print('blue')

    pygame.display.flip()

pygame.quit()