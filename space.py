import pygame
import os

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 2554)

lambai = 500
chodai = 900

Spaceship_ki_lambai, Spaceship_ki_chodai= 55, 40

FPS = 60

display = pygame.display.set_mode((chodai, lambai))
pygame.display.set_caption("PEW PEW GAME")



clock= pygame.time.Clock()

yellow_spaceship = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (Spaceship_ki_chodai, Spaceship_ki_lambai)), 270)

red_spaceship = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (Spaceship_ki_chodai, Spaceship_ki_lambai)), 90)

def drawing(red, yellow):
    display.fill((blue))
    display.blit(yellow_spaceship, (yellow.x, yellow.y))
    display.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()


def maze_kero():

    red = pygame.Rect(100, 300, Spaceship_ki_chodai, Spaceship_ki_chodai)
    yellow = pygame.Rect(700, 300, Spaceship_ki_chodai, Spaceship_ki_chodai)

    haar_gye_aap = False

    while not haar_gye_aap:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                haar_gye_aap = True

        #red.x += 1
        #red.y += -1
        #yellow.x += -1

        drawing(red, yellow)
       
        
    clock.tick(FPS)

maze_kero()

