from mimetypes import init
from tkinter import Scale
from turtle import speed
import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 500
ground_image_size = (screen_width,100)
bg_image_size = (screen_width, screen_height)
sprite_size = (50, 50)
sprite_x = screen_width/3



all_sprites = pygame.sprite.LayeredUpdates()
player_sprite = pygame.sprite.LayeredUpdates()


sprite_y = screen_height/2
class Player(pygame.sprite.Sprite):
    def __init__(self, player_y, player_x ):
        self.groups = all_sprites, player_sprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = player_x
        self.y = player_y
        self.width = 50
        self.height = 50
        self._layer = 10
        self.image = pygame.surface.Surface((self.width,self.height), pygame.SRCALPHA)
        self.image.blit(sprite, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x 
        self.rect.y = self.y
        self.speed = 0
        self.gravity = 1

    def update(self):
        self.movement()
        print(self.rect.x, self.rect.y)
    
    def movement(self):   
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.speed = 5   
        
        if self.speed > 0.1: 
            self.rect.y -= self.speed

        self.speed = self.speed * 0.95
        self.rect.y += self.gravity

            

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappig Fågel')


#ladda bilder
bg = pygame.image.load('img/bg_fancy.png') 
ground_image = pygame.image.load('img/ground_image_1.png')
sprite = pygame.image.load('img/game_sprite.png')

#skala(?) bilder
bg = pygame.transform.scale(bg, bg_image_size)
ground_image = pygame.transform.scale(ground_image, ground_image_size)
sprite = pygame.transform.scale(sprite, sprite_size )



i=0
player = Player(100, 100)
run = True
while run:
    screen.blit(bg, (0,0))
    screen.blit(ground_image, (i,400))
    all_sprites.draw(screen)

    all_sprites.update()
    
    

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

