#import pygame
import pygame, sys
from pygame.locals import *
from sys import exit
from random import randint

#initial screen size
screen_width = 1150
screen_height = 740

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Kill The Flag - Monster Edition")

# This is a list of 10 numbers
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This is a list of 10 random numbers
numbers = [randint(1, 100) for i in range(10)]

#render images
redtank = pygame.image.load("redtank.png")
greentank = pygame.image.load("greentank.png")
bullet = pygame.image.load("bullet.png")
#resize redtank image
redtank = pygame.transform.scale(redtank, (132, 90))
#resize greentank image
greentank = pygame.transform.scale(greentank, (132, 90))


while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("times new roman", 40)
    # text_surface = font.render(str(numbers), True, (0, 255, 0))
    # x = 0
    # y = (480 - text_surface.get_height()) / 2
    # screen.blit(text_surface, (x, y))
    # pygame.display.update()


    #display redtank image on the bottom right of the screen
    screen.blit(redtank, (screen_width - redtank.get_width() -25, screen_height - redtank.get_height()))
    #display greentank image on the bottom left of the screen
    screen.blit(greentank, (25, screen_height - greentank.get_height()))

    pygame.display.update()

