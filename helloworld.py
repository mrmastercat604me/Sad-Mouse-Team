import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Hello World Project') #TAB NAME
display_surface = pygame.display.set_mode((500,500)) #WINDOW SIZE
font = pygame.font.Font(None, 32) #FONT
text = font.render("Hello World!", True,(255,255,255),(0,0,0))
textRect = text.get_rect()
textRect.center = (500//2,500//2)
while True:
  display_surface.fill((0,0,0))
  display_surface.blit(text,textRect)
  for event in pygame.event.get():
    if event.type == QUIT: #IF QUIT, QUIT.
      pygame.quit()
      sys.exit()
  pygame.display.update()
