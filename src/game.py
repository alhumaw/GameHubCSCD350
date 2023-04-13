from pong import start_pong
import pygame, sys
from Button import Button
from main import *


# when play button is clicked
def play():
    while True:
        # constantly obtain position of the mouse cursor
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # overwrite the screen with a black overlay
        window.fill("black")
        PLAY_TEXT = get_font(45).render("This is the play screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # render text to screen
        window.blit(PLAY_TEXT, PLAY_RECT)
        PONG_GAME = Button(image=None, pos=(640, 360),
                           text_input="PONG", font=get_font(75), base_color="White", hovering_color="Green")
        # clicking this will return back to the main menu
        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        # change the color when the mouse is hovering
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(window)
        PONG_GAME.changeColor(PLAY_MOUSE_POS)
        PONG_GAME.update(window)

        for event in pygame.event.get():
            # if you press the "X" button, the game will exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if the mouse clicks the back button, return to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PONG_GAME.checkForInput(PLAY_MOUSE_POS):
                    start_pong(window)
        # constantly update the screen. this is the critical piece of creating a game loop
        pygame.display.update()

