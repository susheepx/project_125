#import pygame
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
pygame.display.set_caption("Kill The Flag - Monster Edition")

# This is a list of 10 numbers
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This is a list of 10 random numbers
numbers = [randint(1, 100) for i in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("times new roman", 40)
    text_surface = font.render(str(numbers), True, (0, 255, 0))
    x = 0
    y = (480 - text_surface.get_height()) / 2
    screen.blit(text_surface, (x, y))
    pygame.display.update()

