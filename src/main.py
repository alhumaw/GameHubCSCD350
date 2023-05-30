import pygame, sys
from pygame import mixer

from Button import Button
from game import play as play_game

pygame.init()
# This is the screen width and height of window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# The caption for the window
pygame.display.set_caption("Menu")

# Background image
BG = pygame.image.load("res/BG.png")


# modular ability to change the size of the font
def get_font(size):
    return pygame.font.Font("res/fonts/chary___.ttf", size)


vol = .7




# options menu TBD
def options(vol):
    while True:
        # constantly record the mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # white overlay
        window.fill("white")
        # text rendering
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(cxenter=(640, 260))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # back button
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        VOLUME = Button(image=None, pos=(640, 560),
                        text_input="VOLUME", font=get_font(75), base_color="Black", hovering_color="Black")
        VOLUME_UP = Button(image=None, pos=(760, 550),
                           text_input="+", font=get_font(75), base_color="Black", hovering_color="Green")
        VOLUME_DOWN = Button(image=None, pos=(500, 550),
                             text_input="-", font=get_font(75), base_color="Black", hovering_color="Green")

        # changing colors on hover
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(window)
        VOLUME.changeColor(OPTIONS_MOUSE_POS)
        VOLUME.update(window)
        VOLUME_UP.changeColor(OPTIONS_MOUSE_POS)
        VOLUME_UP.update(window)
        VOLUME_DOWN.changeColor(OPTIONS_MOUSE_POS)
        VOLUME_DOWN.update(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return vol
                if VOLUME_UP.checkForInput(OPTIONS_MOUSE_POS):
                    vol += .1
                    mixer.music.set_volume(vol)
                if VOLUME_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    vol -= .1
                    mixer.music.set_volume(vol)

        pygame.display.update()


def main_menu(vol=.7):
    increase = True
    mixer.init()
    mixer.music.load("res/menu_music.mp3")
    mixer.music.set_volume(vol)
    mixer.music.play()
    menu_x = -400
    pygame.display.set_caption("Menu")
    play_pos = 250
    while True:
        # draw the screen with the requested background at this position(0,0)
        window.blit(BG, (0, 0))
        menu_x += 4
        # record mouse position on each update
        mouse_pos = pygame.mouse.get_pos()
        # render text
        if menu_x <= SCREEN_WIDTH - 800:
            menu_x = menu_x
        if menu_x >= SCREEN_WIDTH:
            menu_x = -menu_x
        MENU_TEXT = get_font(100).render("ARCADE ADVENTURE", True, "#fbfbfb")
        MENU_RECT = MENU_TEXT.get_rect(center=(menu_x + 640, 100))
        # buttons, add this background, at the position, with this text, this font size, with this color, and when I hover use this color
        PLAY_BUTTON = Button(image=pygame.image.load("res/Play Rect.png"), pos=(640, play_pos),
                             text_input="PLAY", font=get_font(100), base_color="#48ea02", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pygame.image.load("res/Play Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(100), base_color="#48ea02", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("res/Play Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(100), base_color="#48ea02", hovering_color="White")

        # draw our main menu text
        window.blit(MENU_TEXT, MENU_RECT)

        # constantly update the state for hovering on the buttons
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(window)

        # this is just constantly checking for inputs on each update, waiting for a response to do something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play_game(window)

                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    vol = options(vol)
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
        if increase:
            play_pos += .1
            if play_pos > 280:
                increase = False
        else:
            play_pos -= .1
            if play_pos < 250:
                increase = True

        pygame.display.update()


def start_options():
    from options import options
    options(window, True)


# main menu call
main_menu()
