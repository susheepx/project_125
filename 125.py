#import pygame
import pygame, sys
from pygame.locals import *
from sys import exit
from random import randint

#----- Initialize variables -----

#initial screen size
screen_width = 1350
screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Kill The Flag - Monster Edition")

#render images
redtank = pygame.image.load("redtank.png").convert_alpha()
greentank = pygame.image.load("greentank.png").convert_alpha()
Lbullet = pygame.image.load("monstergreen.png").convert_alpha()
Rbullet = pygame.image.load("monsterpink.png").convert_alpha()
#transform images
redtank = pygame.transform.scale(redtank, (132, 90))
greentank = pygame.transform.scale(greentank, (132, 90))
Lbullet = pygame.transform.scale(Lbullet, (30, 25))
Rbullet = pygame.transform.scale(Rbullet, (30, 25))

clock = pygame.time.Clock()

#left side bullet variables: the initial x cord, init_h = initial height, Lbullet_v = Lbullets velocity, Lbullet_path = y cord
Lbullet_x = 125
Linit_h = 1028.41
Lbullet_v = 2.45
Lbullet_path = (1/550*(Lbullet_x**2))-(Lbullet_v*Lbullet_x)+Linit_h
IsLbulletFired = False

#right side bullet variables: the initial x cord, init_h = initial height, Lbullet_v = Lbullets velocity, Lbullet_path = y cord
# Rbullet_x = 0
# Rbullet_actualx = 1000
# init_h = 700
# Rbullet_v = 2.4
# Rbullet_path = (6/2500*(Rbullet_x**2))-(Rbullet_v*Rbullet_x)+init_h
# IsRbulletFired = False

#----- Functions -----
def Lbullet_move(x, y):
    global Lbullet_x, Lbullet_path, IsLbulletFired, Linit_h, Lbullet_v
    #+125 for the tank width
    screen.blit(Lbullet, (x, y))
    Lbullet_x += 2
    Lbullet_path = (1/550*(Lbullet_x**2))-(Lbullet_v*Lbullet_x)+Linit_h
    print(Lbullet_x, Lbullet_path)
    if Lbullet_x > screen_width or Lbullet_path > screen_height:
        IsLbulletFired = False
        Lbullet_x = 125
        Lbullet_path = 1028.41


# def Rbullet_move(x, y):
#     global Rbullet_x, Rbullet_path, IsRbulletFired, init_h, Rbullet_v, Rbullet_actualx
#     #+125 for the tank width
#     screen.blit(Rbullet, (x, y))
#     Rbullet_x += 2
#     Rbullet_actualx -= 1
#     Rbullet_path = (6/2500*(Rbullet_x**2))-(Rbullet_v*Rbullet_x)+init_h
#     if Rbullet_x > screen_width or Rbullet_path > screen_height:
#         IsRbulletFired = False
#         Rbullet_x = 0
#         Rbullet_actualx = 1000
#         Rbullet_path = 750

#----- Main -----
#needed to keep the screen open
#main program loop     
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
                IsLbulletFired = True
            # elif event.key == K_w:
            #     if (Lbullet_v < 3.2):    
            #         Lbullet_v += 0.1
            #     print(Lbullet_v)
            # elif event.key == K_s:
            #     if(Lbullet_v > 1):
            #         Lbullet_v -= 0.1
            #     print(Lbullet_v)
            # elif event.key == K_RSHIFT:
            #     IsRbulletFired = True
            # elif event.key == K_UP:
            #     if (Rbullet_v < 3.2):    
            #         Rbullet_v += 0.1
            #     print(Rbullet_v)
            # elif event.key == K_DOWN:
            #     if(Rbullet_v > 1):
            #         Rbullet_v -= 0.1
            #     print(Rbullet_v)

    #runs the corresponding function when left or right shift is pressed
    if (IsLbulletFired):
        Lbullet_move(Lbullet_x, Lbullet_path)
        print(Lbullet_x, Lbullet_path)
    # if (IsRbulletFired):
    #     Rbullet_move(Rbullet_actualx, Rbullet_path)
    
    # #display the current Lbullet velocity
    # round_LbulletV = round(Lbullet_v, 10)
    # text = font.render("Lbullet velocity: " + str(round_LbulletV), True, (255, 255, 255))
    # screen.blit(text, (0, 0))
   
    # #display the current Rbullet velocity
    # round_RbulletV = round(Rbullet_v, 10)
    # text = font.render("Rbullet velocity: " + str(round_RbulletV), True, (255, 255, 255))
    # screen.blit(text, (0, 40))
    
    #display the tanks
    screen.blit(greentank, (25, screen_height - greentank.get_height()))
    screen.blit(redtank, (screen_width - redtank.get_width() - 25, screen_height - redtank.get_height()))

    pygame.display.update()