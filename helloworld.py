import pygame
from pygame.locals import *
import sys
pygame.init()
DISPLAYSURF = pygame.display.set_mode((200,200))
pygame.display.set_caption('Hello World')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
