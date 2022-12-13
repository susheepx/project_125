#import pygame
import pygame, sys
from pygame.locals import *
from sys import exit
from random import randint
import random as r

#----- Initialize variables -----

#initial screen size
screen_width = 1350
screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kill The Flag - Monster Edition")

clock = pygame.time.Clock()



#render images
redtank = pygame.image.load("redtank.png").convert_alpha()
greentank = pygame.image.load("greentank.png").convert_alpha()
Lbullet = pygame.image.load("monstergreen.png").convert_alpha()
Rbullet = pygame.image.load("monsterpink.png").convert_alpha()
Lmonster = pygame.image.load("Rtargetmonster.png").convert_alpha()
Rmonster = pygame.image.load("Ltargetmonster.png").convert_alpha()
menu = pygame.image.load("menu.png").convert_alpha()
RedWin = pygame.image.load("RedWin.png").convert_alpha()
GreenWin = pygame.image.load("GreenWin.png").convert_alpha()
Tie = pygame.image.load("Tie.png").convert_alpha()
#transform images
redtank = pygame.transform.scale(redtank, (132, 90))
greentank = pygame.transform.scale(greentank, (132, 90))
Lbullet = pygame.transform.scale(Lbullet, (30, 25))
Rbullet = pygame.transform.scale(Rbullet, (30, 25))
Lmonster = pygame.transform.scale(Lmonster, (150, 150))
Rmonster = pygame.transform.scale(Rmonster, (150, 150))


#game object rects
Rmonster_rect = pygame.Rect(1200, 300, 75 , 65)
#(+47, +67) to account for center of the monster image
Rmonster_rect.center = (Rmonster_rect.center[0] + 47, Rmonster_rect.center[1] + 67)
Lmonster_rect = pygame.Rect(0, 300, 75, 65)
#(+47, +67) to account for center of the monster image
Lmonster_rect.center = (Lmonster_rect.center[0] + 47, Lmonster_rect.center[1] + 67)
Lbullet_rect = pygame.Rect(0, 0, 30, 25)
Rbullet_rect = pygame.Rect(0, 0, 30, 25)

#screen variables
screen_type = ['menu', 'game', 'end']
current_screen = screen_type[0]

#left side bullet variables
Lbullet_x = 0
Linit_h = 750
Lbullet_v = 2
Lbullet_path = (1/550*(Lbullet_x**2))-(Lbullet_v*Lbullet_x)+Linit_h
IsLbulletFired = False
Lmonster_hit = False

#right side bullet variables
Rbullet_x = 0
Rbullet_actualx = 1185
Rinit_h = 750
Rbullet_v = 2
Rbullet_path = (1/550*(Lbullet_x**2))-(Rbullet_v*Rbullet_x)+Rinit_h
IsRbulletFired = False

#monster variables
Rmonster_x = 1200
Rmonster_y = 300
Lmonster_x = 0
Lmonster_y = 300

#points variables
Lpoints = 0
Rpoints = 0

#timer variables
counter = 20
pygame.time.set_timer(pygame.USEREVENT, 1000)
timertext = "20".rjust(3)

#----- Functions -----

#called when the left shift key is pressed, fires bullet
def Lbullet_move(x, y):
    global Lbullet_x, Lbullet_path, IsLbulletFired, Linit_h, Lbullet_v
    screen.blit(Lbullet, (x, y))
    Lbullet_x += 3
    Lbullet_path = (1/550*(Lbullet_x**2))-(Lbullet_v*Lbullet_x)+Linit_h
    #when bullet is off screen, reset variables
    if Lbullet_x > screen_width or Lbullet_path > screen_height:
        IsLbulletFired = False
        Lbullet_x = 0
        Lbullet_path = 750

#called when the right shift key is pressed, fires bullet
def Rbullet_move(x, y):
    global Rbullet_x, Rbullet_path, IsRbulletFired, Linit_h, Rbullet_v, Rbullet_actualx
    screen.blit(Rbullet, (x, y))
    Rbullet_x += 3
    Rbullet_actualx -= 3
    Rbullet_path = (1/550*(Rbullet_x**2))-(Rbullet_v*Rbullet_x)+Rinit_h
    #when bullet is off screen, reset variables
    if Rbullet_x > screen_width or Rbullet_path > screen_height:
        IsRbulletFired = False
        Rbullet_x = 0
        Rbullet_actualx = 1185
        Rbullet_path = 750

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
        #counts down the timer
        if event.type == pygame.USEREVENT and current_screen == screen_type[1]: 
            counter -= 1
            timertext = str(counter).rjust(3) if counter > 0 else 'heheheha'
        #checks if the user presses a key
        #checks during menu screen
        if event.type == KEYDOWN and current_screen == screen_type[0]:
            if event.key == K_SPACE:
                current_screen = screen_type[1]
        #checks during game screen
        elif event.type == KEYDOWN and current_screen == screen_type[1]:
            if event.key == K_LSHIFT:
                IsLbulletFired = True
            elif event.key == K_w:
                if (Lbullet_v < 2.9 and IsLbulletFired == False):    
                    Lbullet_v += 0.1
                print(Lbullet_v)
            elif event.key == K_s:
                if(Lbullet_v > .75 and IsLbulletFired == False):
                    Lbullet_v -= 0.1
                print(Lbullet_v)
            elif event.key == K_RSHIFT:
                IsRbulletFired = True
            elif event.key == K_UP:
                if (Rbullet_v < 2.9 and IsRbulletFired == False):    
                    Rbullet_v += 0.1
                print(Rbullet_v)
            elif event.key == K_DOWN:
                if(Rbullet_v > .75 and IsRbulletFired == False):
                    Rbullet_v -= 0.1
                print(Rbullet_v)
        

    #shoots bullet when left or right shift is pressed
    if (IsLbulletFired):
        Lbullet_move(Lbullet_x +125, Lbullet_path)
    if (IsRbulletFired):
        Rbullet_move(Rbullet_actualx, Rbullet_path)

    #checks if the Lbullet has hit the Rmonster 
    Lbullet_rect = pygame.Rect(Lbullet_x +125, Lbullet_path, 30, 25)
    if (Lbullet_rect.colliderect(Rmonster_rect)):
        print("hit")
        IsLbulletFired = False
        Lbullet_x = 0
        Lbullet_path = 750
        Lpoints += 1
        Lmonster_hit = True
        #randomize Rmonster x and y
        Rmonster_x = r.randint(900, 1200)
        Rmonster_y = r.randint(0, 700)
        Rmonster_rect = pygame.Rect(Rmonster_x +47, Rmonster_y +67, 75, 75)

    else: 
        screen.blit(Rmonster, (Rmonster_x, Rmonster_y))
    
    #checks if the Rbullet has hit the Lmonster
    Rbullet_rect = pygame.Rect(Rbullet_actualx, Rbullet_path, 30, 25)
    if (Rbullet_rect.colliderect(Lmonster_rect)):
        print("hit")
        IsRbulletFired = False
        Rbullet_x = 0
        Rbullet_actualx = 1185
        Rbullet_path = 750
        Rpoints += 1
        Lmonster_hit = True
        #randomize Lmonster x and y
        Lmonster_x = r.randint(0, 400)
        Lmonster_y = r.randint(0, 700)
        Lmonster_rect = pygame.Rect(Lmonster_x +47, Lmonster_y +67, 75, 75)
    else:
        screen.blit(Lmonster, (Lmonster_x, Lmonster_y))
        

    #display game screen text (velocity, points, timer)

        # the current Lbullet velocity
    round_LbulletV = round(Lbullet_v, 10)
    text = font.render("Velocity: " + str(round_LbulletV), True, (255, 255, 255))
    screen.blit(text, (0, 650))
        # the current Rbullet velocity
    round_RbulletV = round(Rbullet_v, 10)
    text = font.render("Velocity: " + str(round_RbulletV), True, (255, 255, 255))
    screen.blit(text, (1140, 650))
        # the current points
    text = font.render("Points: " + str(Lpoints), True, (255, 255, 255))
    screen.blit(text, (0, 0))
    text = font.render("Points: " + str(Rpoints), True, (255, 255, 255))
    screen.blit(text, (1175, 0))

        # the current timer
    if (counter > 5):
        screen.blit(font.render('Time:' + timertext, True, (255,255,255)), (550, 20))
    #changes timer color to red when 5 seconds are left
    else:
        screen.blit(font.render('Time:' + timertext, True, (255,0,0)), (550, 20))
    
    #display the tank
    screen.blit(greentank, (25, screen_height - greentank.get_height()))
    screen.blit(redtank, (screen_width - redtank.get_width() - 25, screen_height - redtank.get_height()))

    #displays the menu screen as long as space isn't pressed
    if (current_screen == screen_type[0]):
        screen.blit(menu, (0, 0))
    
    #displays end screen when timer runs out
    if (counter == 0):
        if (Lpoints > Rpoints):
            screen.blit(GreenWin, (0, 0))
        elif (Lpoints < Rpoints):
            screen.blit(RedWin, (0, 0))
        else:
            screen.blit(Tie, (0, 0))
        current_screen = screen_type[2]


    
    pygame.display.flip()
    
    # pygame.display.update()