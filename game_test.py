from asyncio.windows_utils import pipe
from mimetypes import init
from random import random
import random
from re import S
from tkinter import Scale
from turtle import speed

import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 700
        self.screen_height = 500
        ground_image_size = (self.screen_width,100)
        bg_image_size = (self.screen_width, self.screen_height)
        sprite_size = (50, 50)
        self.sprite_x = self.screen_width/3
        self.sprite_y = self.screen_height/2
        
        self.pipe_size_y = 350
        self.pipe_gap = 200

        self.pipe_new = False

        self.run = True
        self.play = False

        self.score = 0
        self.font = pygame.font.Font("comici.ttf", 32)

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.i=0
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player_sprite = pygame.sprite.LayeredUpdates()
        self.pipe_sprite = pygame.sprite.LayeredUpdates()
       
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Flappig Fågel')
        #laddar bilder
        bg = pygame.image.load('img/bg_fancy.png') 
        ground_image = pygame.image.load('img/ground_image_1.png')
        sprite = pygame.image.load('img/game_sprite.png')
        start_screen =  pygame.image.load('img/start_screen.png')
        end_screen =  pygame.image.load('img/game_over_screen.png')
        pipe = pygame.image.load('img/better_pipe.png')
        #skalar bilder
        self.bg = pygame.transform.scale(bg, bg_image_size)
        self.ground_image = pygame.transform.scale(ground_image, ground_image_size)
        self.sprite = pygame.transform.scale(sprite, sprite_size )
        self.end_screen = pygame.transform.scale(end_screen,(self.screen_width,self.screen_height))
        self.start_screen = pygame.transform.scale(start_screen,(self.screen_width,self.screen_height))
        self.pipe = pygame.transform.scale(pipe,(50 ,self.pipe_size_y)) 

    def draw(self,):
        if self.pipe_new:
           
            pipe_spawn = random.randint(175 , 430)
            Pipe(self, 700, pipe_spawn)
            Pipe(self, 700, pipe_spawn - self.pipe_gap - self.pipe_size_y)
            self.pipe_new = False
 
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.ground_image, (self.i,450))
        self.screen.blit(self.ground_image,(self.screen_width+self.i,450))
        self.all_sprites.draw(self.screen)
        if (self.i==-self.screen_width):
            self.screen.blit(self.ground_image,(self.screen_width+self.i,450) )
            self.i=0
        self.i-=2

        self.screen.blit(self.font.render("SCORE:" + str(self.score//2), True, (255,255,0)), (self.screen_width/2-60, 10))

        self.clock.tick(self.fps)
        pygame.display.update()

    def new(self):
        Player(self, 100, 100)
        Pipe(self, 700, 350)
        Pipe(self, 700, -250)
        self.score = 0
        self.play = True

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
                self.run = False

    def main(self):
        while self.play:
            self.event()
            self.update()
            self.draw()
        

    def update(self):
        self.all_sprites.update()

    def start(self):
       intro = True
       while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                self.run = False
        self.screen.blit(self.start_screen, (0,0))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
              intro = False 
        self.clock.tick(self.fps)
        pygame.display.update()

    

    def end(self):
        Restart_button = Button(self.screen_width/2-150, self.screen_height/2+10, 300, 100, (255,255,255), (0,0,0,0), "Try Again", 40)
        while self.run and not self.play :
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False


         mouse_pos = pygame.mouse.get_pos()
         mouse_pressed = pygame.mouse.get_pressed()
         
         if Restart_button.isPressed(mouse_pos, mouse_pressed):
             for sprite in self.all_sprites:
                 sprite.kill()
             self.new() 
         self.screen.blit(self.bg, (0,0))
         self.screen.blit(self.ground_image, (self.i,450))
         self.screen.blit(self.ground_image,(self.screen_width+self.i,450))
         self.all_sprites.draw(self.screen)
         self.screen.blit(self.end_screen, (0,0))
         self.screen.blit(self.font.render("SCORE:" + str(self.score//2), True, (255,255,0)), (self.screen_width/2-60, 10))
         self.screen.blit(Restart_button.image, Restart_button.rect)
         self.clock.tick(self.fps)
         pygame.display.update()







class Pipe(pygame.sprite.Sprite):
   def __init__(self, game, pipe_x, pipe_y ):
        self.game = game
        self.groups = self.game.all_sprites, self.game.pipe_sprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = pipe_x
        self.y = pipe_y
        self.width = 50
        self.height = 350
        self._layer = 10
        self.image = pygame.surface.Surface((self.width,self.height), pygame.SRCALPHA)
        self.image.blit(self.game.pipe, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x 
        self.rect.y = self.y
        self.speed = 2
        self.i = 500

        
       

   def update(self):
        self.movement()
        self.player_score()
        

   def movement(self):
       self.rect.x -= self.speed

       if self.rect.x == 400:
           self.game.pipe_new = True


   def player_score(self):
       if self.rect.x == 100 :
           self.game.score+=1
           
 

      

 
        

class Player(pygame.sprite.Sprite):
    def __init__(self, game, player_y, player_x ):
        self.game = game
        self.groups = self.game.all_sprites, self.game.player_sprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = player_x
        self.y = player_y
        self.width = 50
        self.height = 50
        self._layer = 10
        self.image = pygame.surface.Surface((self.width,self.height), pygame.SRCALPHA)
        self.image.blit(self.game.sprite, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x 
        self.rect.y = self.y
        self.speed = 0
        self.gravity = 5
        
        

    def update(self):
        self.movement()
        self.is_dead()
        
    
    def movement(self):   
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.speed < 5:
            self.speed = 20 
        
        if self.speed > 0.1: 
            self.rect.y -= self.speed

        self.speed = self.speed * 0.90 
        self.rect.y += self.gravity
   
    def is_dead(self):
        if self.rect.y > 400 or self.rect.y < 0:
            self.game.play = False
        if pygame.sprite.spritecollide(self, self.game.pipe_sprite, False):
           self.game.play = False
        

    




class Button:
    def __init__(self, x, y, width, height, fg ,bg, content, font_size):
        self.font = pygame.font.Font("comici.ttf",font_size)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height),pygame.SRCALPHA)
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center =(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)
    
    def isPressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False



g = Game()

g.start()
g.new()
while g.run:
    g.main()
    g.end()
pygame.quit()

