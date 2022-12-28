import pygame
from pygame.locals import *
import os
import sys

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.transform.smoothscale(pygame.image.load(image_file), (screen_width, screen_height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def choosing_background_pic(screen_width, screen_height, type_background):
    print(screen_width, screen_height, type_background)
    if type_background == "desert":
        BackGround_desert = Background('background_images_uno/desert.jpg', [0,0], screen_width, screen_height)
        return BackGround_desert
    elif type_background == "forest": 
        BackGround_forest = Background('background_images_uno/forest.jpg', [0,0], screen_width, screen_height)
        return BackGround_forest
    elif type_background == "snow":
        BackGround_snow = Background('background_images_uno/snow.jpg', [0,0], screen_width, screen_height)
        return BackGround_snow
