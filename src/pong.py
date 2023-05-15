import pygame
import random

from pygame import mixer

from options import options


def start_pong(window):
    mixer.init()
    width = 1280
    height = 720
    pause = False
    saved_x_velocity = 0
    saved_y_velocity = 0
    pygame.font.get_default_font()
    ffUp = pygame.image.load("res/fastForward.png")
    new_width, new_height = ffUp.get_width() * 1.6, ffUp.get_height() * 1.6
    ffUp = pygame.transform.scale(ffUp, (new_width, new_height))
    crash_sound = pygame.mixer.Sound("res/blip.mp3")
    power = pygame.mixer.Sound("res/powerup.mp3")
    power.set_volume(.3)
    rect1X = 15
    rect1Y = 240
    rect2X = 1240
    rect2Y = 240

    rect1W = 25
    rect1H = 225
    rect2W = 25
    rect2H = 225

    powerX = random.randint(100, 400)
    powerY = random.randint(100, 200)

    color = (255, 255, 255)

    p1Up = False
    p1Down = False

    clock = pygame.time.Clock()

    circleX = width / 2
    circleY = height / 2
    circleR = 40
    xVelocity = 6
    yVelocity = 6
    p1Score = 0
    p2Score = 0
    maxScore = 3
    red = 0
    green = 0
    blue = 0
    powerTimer = 0
    ai_paddle_speed = 4

    while True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pause = not pause
                    if pause:
                        saved_x_velocity = xVelocity
                        saved_y_velocity = yVelocity
                        xVelocity = 0
                        yVelocity = 0
                        state = options(window, pause)
                        if not state:
                            xVelocity = saved_x_velocity
                            yVelocity = saved_y_velocity
                if event.key == pygame.K_w:
                    p1Up = True
                if event.key == pygame.K_s:
                    p1Down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1Up = False
                if event.key == pygame.K_s:
                    p1Down = False

            if event.type == pygame.QUIT:
                exit()
        circleX -= xVelocity
        circleY -= yVelocity
        saveCircleY = circleY - 150
        if saveCircleY < rect2Y:
            rect2Y -= ai_paddle_speed
        elif saveCircleY > rect2Y:
            rect2Y += ai_paddle_speed

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

        game_score = pygame.font.Font('res/fonts/chary___.ttf', 72)
        winner = pygame.font.Font('res/fonts/chary___.ttf', 72)
        text = game_score.render(f"PLAYER 1: {p1Score} | PLAYER 2: {p2Score}", True, (255, 255, 255))
        window.fill((red, green, blue))
        window.blit(text, (width / 2 - 400, 0))
        c1 = pygame.draw.circle(window, color, (circleX, circleY), circleR)
        r1 = pygame.draw.rect(window, color, (rect1X, rect1Y, rect1W, rect1H))
        r2 = pygame.draw.rect(window, color, (rect2X, rect2Y, rect2W, rect2H))
        collide1 = r1.colliderect(circleX - circleR, circleY - circleR, circleR * 2, circleR * 2)
        collide2 = r2.colliderect(circleX - circleR, circleY - circleR, circleR * 2, circleR * 2)
        window.blit(ffUp, (powerX, powerY))

        power_rect = pygame.Rect(powerX, powerY, new_width, new_height)

        if power_rect.collidepoint(circleX + circleR / 2, circleY + circleR / 2):
            power.play()
            xVelocity *= 1.3
            yVelocity *= 1.3
            powerX = random.randint(100, 400)
            powerY = random.randint(100, 200)
            power_rect = pygame.Rect(powerX, powerY, ffUp.get_width(), ffUp.get_height())

        if yVelocity > 0 and circleY <= 0 + circleR:
            yVelocity = -yVelocity
        if yVelocity < 0 and circleY >= 720 - circleR:
            yVelocity = -yVelocity

        if circleX <= 0:
            circleX = width / 2
            circleY = height / 2
            xVelocity = 4
            yVelocity = 4
            yVelocity = -yVelocity
            xVelocity = -xVelocity
            p2Score += 1

        if circleX >= 1280:
            circleX = width / 2
            circleY = height / 2
            xVelocity = 4
            yVelocity = 4
            yVelocity = -yVelocity
            xVelocity = -xVelocity
            p1Score += 1

        if p1Score >= maxScore:
            text1 = winner.render(f"PLAYER 1 WINS.", True, (255, 255, 255))
            window.blit(text1, (200, 150))
            xVelocity = 0
            yVelocity = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p1Score = 0
                    p2Score = 0
                    xVelocity = 4
                    yVelocity = 4

        if p2Score >= maxScore:
            text1 = winner.render(f"PLAYER 2 WINS.", True, (255, 255, 255))
            window.blit(text1, (200, 150))
            xVelocity = 0
            yVelocity = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p1Score = 0
                    p2Score = 0
                    xVelocity = 4
                    yVelocity = 4

        if collide1:
            crash_sound.play()
            xVelocity = -xVelocity
            circleX = rect1X + rect1W + circleR
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

        else:
            color = (255, 255, 255)

        if collide2:
            crash_sound.play()
            xVelocity = -xVelocity
            circleX = rect2X - circleR
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
        else:
            color = (255, 255, 255)

        pygame.display.flip()

        clock.tick(60)
