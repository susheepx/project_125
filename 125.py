#import pygame
import pygame, sys
from pygame.locals import *
from sys import exit
from random import randint

#----- Initialize variables -----

#initial screen size
screen_width = 1150
screen_height = 740

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Kill The Flag - Monster Edition")

#render images
redtank = pygame.image.load("redtank.png").convert_alpha()
greentank = pygame.image.load("greentank.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()
#transform images
redtank = pygame.transform.scale(redtank, (132, 90))
greentank = pygame.transform.scale(greentank, (132, 90))
bullet = pygame.transform.scale(bullet, (30, 30))
bullet = pygame.transform.rotate(bullet, -90)

clock = pygame.time.Clock()

#bullet variables
    #left tank bullets
Lbullet_x = 125
Lbullet_y = screen_height -50
Lbulletx_change = 0
Lbullety_change = 20
isLBulletFired = False
    #right tank bullets
Rbullet_x = screen_width - 155
Rbullet_y = screen_height -50
Rbulletx_change = 0
Rbullety_change = 20
isRBulletFired = False


#----- Functions -----
def shoot_bullet(x, y):
    global Lbullet_x, Lbullet_y
    screen.blit(bullet, (x, y))


#----- Main -----
#needed to keep the screen open
while True:

    #draws the background color          
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("times new roman", 40)

    for event in pygame.event.get():
        #closes screen if user clicks the x or esc
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_LSHIFT:
                isLBulletFired = True
            elif event.key == K_RSHIFT:
                isRBulletFired = True
    #if left shift is pressed, fire bullet   
    if (isLBulletFired == True):
        Lbullet_x += .75
        shoot_bullet(Lbullet_x, Lbullet_y)
        if Lbullet_x > screen_width:
            isLBulletFired = False
            Lbullet_x = 125
    #if right shift is pressed, fire bullet
    if (isRBulletFired == True):
        Rbullet_x -= .75
        shoot_bullet(Rbullet_x, Rbullet_y)
        if Rbullet_x < 0:
            isRBulletFired = False
            Rbullet_x = screen_width - 155
    

    #display redtank image on the bottom right of the screen and greentank on bottom left
    screen.blit(redtank, (screen_width - redtank.get_width() -25, screen_height - redtank.get_height()))
    screen.blit(greentank, (25, screen_height - greentank.get_height()))
    

    pygame.display.update()

