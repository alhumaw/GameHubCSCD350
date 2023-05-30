import pygame
import random
from options import options

from pygame import mixer
from leaderboard import set_score

def start_space_invaders(window):
    mixer.init()
    width = 1280
    height = 720
    invader = pygame.image.load("res/red.png")
    player = pygame.image.load("res/pngegg.png")
    clock = pygame.time.Clock()


    playerX = 0
    p1Left = False
    p1Right = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p1Left = True
                if event.key == pygame.K_d:
                    p1Right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1Left = False
                if event.key == pygame.K_s:
                    p1Right = False
            if event.type == pygame.QUIT:
                exit()

        if p1Left:
            playerX -= 5
        if p1Right:
            playerX += 5

        window.fill((0, 0, 0))
        window.blit(player, (playerX, height - player.get_height()))


        pygame.display.flip()

        clock.tick(60)


