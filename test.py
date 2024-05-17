
from asyncio.windows_utils import pipe
from mimetypes import init
from random import random
import random
from re import S
from tkinter import Scale
from turtle import speed
import pygame
from pygame.locals import *
start_screen =  pygame.image.load('img/game_over_screen.png')
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
  
screen.blit(start_screen, (0,0))