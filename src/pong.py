import pygame
from pygame import font
import random

def play():
    pygame.init()
    width = 640
    height = 480
    window = pygame.display.set_mode((width,height))
    pygame.font.get_default_font()
    ffUp = pygame.image.load("res/fastForward.png")
    crash_sound = pygame.mixer.Sound("res/blip.mp3")
    power = pygame.mixer.Sound("res/powerup.mp3")
    rect1X = 15
    rect1Y = 240
    rect2X = 610
    rect2Y = 240

    rect1W = 15
    rect1H = 150
    rect2W = 15
    rect2H = 150

    powerX = random.randint(100,400)
    powerY = random.randint(100,200)


    color = (255,255,255)

    p1Up = False
    p1Down = False
    p2Up = False
    p2Down = False

    clock = pygame.time.Clock()

    circleX = width/2  
    circleY = height/2 
    circleR = 20
    xVelocity = 4
    yVelocity = 4
    p1Score = 0
    p2Score = 0
    maxScore = 3
    red = 0
    green = 0
    blue = 0
    powerTimer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p1Up = True
                if event.key == pygame.K_s:
                    p1Down = True
                if event.key == pygame.K_UP:
                    p2Up = True
                if event.key == pygame.K_DOWN:
                    p2Down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1Up = False
                if event.key == pygame.K_s:
                    p1Down = False
                if event.key == pygame.K_UP:
                    p2Up = False
                if event.key == pygame.K_DOWN:
                    p2Down = False
            


            if event.type == pygame.QUIT:
                exit()
        circleX -= xVelocity
        circleY -= yVelocity




        if p1Up:
            rect1Y -= 5
        if p1Down:
            rect1Y += 5
        if rect1Y <= 0:
            rect1Y = 0
        if rect1Y >= height - rect1H:
            rect1Y = height - rect1H
        if rect2Y <= 0:
            rect2Y = 0
        if rect2Y >= height - rect2H:
            rect2Y = height - rect2H
        if p2Up:
            rect2Y -= 5
        if p2Down:
            rect2Y += 5

        game_score=pygame.font.Font('res/fonts/chary___.ttf',  30)
        winner=pygame.font.Font('res/fonts/chary___.ttf',  30)
        text = game_score.render(f"PLAYER 1: {p1Score} | PLAYER 2: {p2Score}", True, (255,255,255))
        window.fill((red,green,blue))
        window.blit(text,(135,0))
        c1 =pygame.draw.circle(window,color,(circleX,circleY),circleR)
        r1 = pygame.draw.rect(window, color, (rect1X,rect1Y,rect1W,rect1H))
        r2 = pygame.draw.rect(window, color, (rect2X,rect2Y, rect2W, rect2H))
        collide1 = r1.collidepoint(circleX - circleR/2,circleY - circleR/2)
        collide2 = r2.collidepoint(circleX + circleR/2,circleY + circleR/2)
        window.blit(ffUp, (powerX,powerY))

        power_rect = pygame.Rect(powerX, powerY, ffUp.get_width(), ffUp.get_height())

        if power_rect.collidepoint(circleX + circleR/2,circleY + circleR/2):
            power.play()
            xVelocity *= 1.3
            yVelocity *= 1.3
            powerX = random.randint(100,400)
            powerY = random.randint(100,200)
            power_rect = pygame.Rect(powerX, powerY, ffUp.get_width(), ffUp.get_height())

        if yVelocity > 0 and circleY <= 0 + circleR:
            yVelocity = -yVelocity
        if yVelocity < 0 and circleY >= 480 - circleR:
            yVelocity = -yVelocity

        if circleX <= 0:
            circleX = width/2  
            circleY = height/2 
            xVelocity = 4
            yVelocity = 4
            yVelocity = -yVelocity
            xVelocity = -xVelocity
            p2Score += 1



        if circleX >= 640:
            circleX = width/2  
            circleY = height/2
            xVelocity = 4
            yVelocity = 4 
            yVelocity = -yVelocity
            xVelocity = -xVelocity
            p1Score += 1

        if p1Score >= maxScore:
            text1 = winner.render(f"PLAYER 1 WINS.", True, (255,255,255))
            window.blit(text1,(200,150))
            xVelocity = 0
            yVelocity = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p1Score = 0
                    p2Score = 0
                    xVelocity = 4
                    yVelocity = 4

        if p2Score >= maxScore:
            text1 = winner.render(f"PLAYER 2 WINS.", True, (255,255,255))
            window.blit(text1,(200,150))
            xVelocity = 0
            yVelocity = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p1Score = 0
                    p2Score = 0
                    xVelocity = 4
                    yVelocity = 4


        if collide1 :
            crash_sound.play()
            xVelocity = -xVelocity
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
        else:
            color = (255,255,255)

        if collide2:
            crash_sound.play()
            xVelocity = -xVelocity
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
        else:
            color = (255,255,255)  
        pygame.display.flip()

        clock.tick(60)
