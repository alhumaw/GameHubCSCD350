import pygame
import random
from options import options

from pygame import mixer
from leaderboard import set_score


def start_space_invaders(window):
    mixer.init()
    width = 1280
    height = 720
    pause = False
    player = pygame.image.load("res/p1.png")
    clock = pygame.time.Clock()
    count = 100
    playerX = 0
    p1Left = False
    p1Right = False
    bullets = []  # Store bullet positions in a list
    bullet_speed = 8
    invaders = []  # List of invaders, each represented as a dictionary
    invaders_to_remove = []
    bullets_to_remove = []
    numInvaders = 0
    tile_width = tile_height = 64
    tiles = []
    for y in range(0, height, tile_height):
        for x in range(0, width, tile_width):
            tiles.append(Tile(x, y))

    while numInvaders < 30:
        while True:
            x = random.randint(45, 1235)
            y = random.randint(0, 300)
            new_invader = Invader(x, y)

            if all(not invader.rect.colliderect(new_invader.rect) for invader in invaders):
                break

        invaders.append(new_invader)
        numInvaders += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pause = not pause
                    if pause:
                        state = options(window, pause)
                        if not state:
                            print()
                if event.key == pygame.K_a:
                    p1Left = True
                if event.key == pygame.K_d:
                    p1Right = True
                if event.key == pygame.K_SPACE:
                    bullets.append([playerX + player.get_width() // 2, height - player.get_height() - 20])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    p1Left = False
                if event.key == pygame.K_d:
                    p1Right = False
            if event.type == pygame.QUIT:
                exit()

        for bullet in bullets:
            bullet[1] -= bullet_speed

        if p1Left:
            playerX -= 5
        if p1Right:
            playerX += 5

        for invader in invaders:
            for bullet in bullets:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 10)  # Create bullet Rect

                if invader.rect.colliderect(bullet_rect):  # Check for collision
                    invaders_to_remove.append(invader)  # Mark invader for removal
                    bullets_to_remove.append(bullet)  # Mark bullet for removal
                    break

        window.fill((0, 0, 0))
        for tile in tiles:
            tile.draw(window)
        window.blit(player, (playerX, height - player.get_height() - 20))

        for invader in invaders:
            invader.move()
            invader.draw(window)
        for bullet in bullets:
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(bullet[0], bullet[1], 5, 10))

        if len(invaders_to_remove) > 0:
            for invader in invaders_to_remove:
                if invader in invaders:  # Check if invader is still in the list
                    invaders.remove(invader)
        for bullet in bullets_to_remove:
            if bullet in bullets:  # Check if bullet is still in the list
                bullets.remove(bullet)
        invaders_to_remove.clear()  # Clear the list
        bullets_to_remove.clear()  # Clear the list



        pygame.display.flip()

        clock.tick(60)


class Invader:
    invader_image = pygame.image.load("res/red.png")
    width = 1280
    height = 720

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 2
        self.rect = pygame.Rect(x, y, self.invader_image.get_width(), self.invader_image.get_height())

    def move(self):
        if self.x >= Invader.width - Invader.invader_image.get_width():
            self.velocity = -self.velocity
            self.y += Invader.invader_image.get_height()
        if self.x < 0 + Invader.invader_image.get_width() - 10:
            self.velocity = - self.velocity
            self.y += Invader.invader_image.get_height()
        self.x += self.velocity
        self.rect.x = self.x  # Update the Rect object's x position
        self.rect.y = self.y  # Update the Rect object's y position

    def draw(self, window):
        window.blit(self.invader_image, (self.x, self.y))


class Tile:
    BG = pygame.image.load("res/SpaceInvaders_Background.png")

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, window):
        window.blit(self.BG, (self.x,self.y))