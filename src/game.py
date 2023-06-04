from pong import start_pong
from duck import start_duck
from snake import start_snake
from spaceInvaders import start_space_invaders
import pygame, sys
from Button import Button


pygame.mixer.init()
# modular ability to change the size of the font
def get_font(size):
    return pygame.font.Font("res/fonts/chary___.ttf", size)

def play(window):
    while True:
        # constantly obtain position of the mouse cursor
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # overwrite the screen with a black overlay
        window.fill("black")
        PLAY_TEXT = get_font(45).render("Pick A Game To Play", True, "Gold")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        # render text to screen
        window.blit(PLAY_TEXT, PLAY_RECT)
        # clicking this will return back to the main menu
        Game1B = Button(image=None, pos=(250, 350),
                        text_input="Pong", font=get_font(50), base_color="White", hovering_color="Green")

        Game2B = Button(image=None, pos=(620, 350),
                        text_input="Tic-Tac-Toe", font=get_font(50), base_color="White", hovering_color="Green")

        Game3B = Button(image=None, pos=(990, 350),
                        text_input="DOOM", font=get_font(50), base_color="White", hovering_color="Green")

        Game4B = Button(image=None, pos=(250, 650),
                        text_input="Snake", font=get_font(50), base_color="White", hovering_color="Green")

        Game5B = Button(image=None, pos=(620, 650),
                        text_input="Tower Defence", font=get_font(50), base_color="White", hovering_color="Green")

        Game6B = Button(image=None, pos=(990, 650),
                        text_input="Space Inv", font=get_font(50), base_color="White", hovering_color="Green")

        # change the color when the mouse is hovering
        Game1B.changeColor(PLAY_MOUSE_POS)
        Game1B.update(window)

        Game2B.changeColor(PLAY_MOUSE_POS)
        Game2B.update(window)

        Game3B.changeColor(PLAY_MOUSE_POS)
        Game3B.update(window)

        Game4B.changeColor(PLAY_MOUSE_POS)
        Game4B.update(window)

        Game5B.changeColor(PLAY_MOUSE_POS)
        Game5B.update(window)

        Game6B.changeColor(PLAY_MOUSE_POS)
        Game6B.update(window)

        image1 = pygame.image.load("res/pongimg.jpg")
        test1 = pygame.image.load("res/test3.gif")
        TicTac = pygame.image.load("res/TicTacImg.jpg")
        Doom = pygame.image.load("res/DoomImg.jpg")

        #images above buttons
        #window.blit(image1, (50,50))
        window.blit(TicTac, (535, 100))
        window.blit(Doom, (800, 200))

        #attempt at gif

        image_surface = pygame.Surface((image1.get_width(), image1.get_height()))
        image_surface.blit(image1, (0, 0))

        image_x = 155
        image_y = 140

        gif_x = image_x
        gif_y = image_y


        window.blit(image_surface, (image_x, image_y))


        for event in pygame.event.get():
            # if you press the "X" button, the game will exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if the mouse clicks the back button, return to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Game1B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_pong(window)
                if Game5B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_duck(window)
                if Game4B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_snake(window)
                if Game6B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_space_invaders(window)
                #TIC TAC TOE MOUSE INPUT
                if Game2B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_tictactoe(window)

        # constantly update the screen. this is the critical piece of creating a game loo[]
        pygame.display.update()
