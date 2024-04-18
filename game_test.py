from mimetypes import init
from tkinter import Scale
import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 500
ground_image_size = (screen_width,100)
bg_image_size = (screen_width, screen_height)
sprite_size = (50, 50)
sprite_x = screen_width/3


sprite_y = screen_height/2
class sprite
def __init__(self, sprite_y, sprite_x ):
    sprite_y

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappig Fågel')


#ladda bilder
bg = pygame.image.load('img/bg_fancy.png') 
ground_image = pygame.image.load('img/ground_image_1.png')
sprite = pygame.image.load('img/game_sprite.png')


bg = pygame.transform.scale(bg, bg_image_size)
ground_image = pygame.transform.scale(ground_image, ground_image_size)
sprite = pygame.transform.scale(sprite, sprite_size )

i=0
run = True
while run:
    
    screen.blit(bg, (0,0))
    screen.blit(ground_image, (i,400))
    screen.blit(sprite, (sprite_x, sprite_y))
    
    screen.blit(ground_image,(screen_width+i,400))
    if (i==-screen_width):
        screen.blit(ground_image,(screen_width+i,400))
        i=0
    i-=1
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False
         
    pygame.display.update()

pygame.quit()

