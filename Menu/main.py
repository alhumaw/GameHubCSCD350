import pygame, sys
from Button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("res/BG.png")

def get_font(size):
    return pygame.font.Font("res/fonts/chary___.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        window.fill("black")

        PLAY_TEXT = get_font(45).render("This is the play screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640,260))
        window.blit(PLAY_TEXT,PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640,460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color = "Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        window.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        window.blit(BG, (0,0))

        mouse_pos = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640,100))

        PLAY_BUTTON = Button(image=pygame.image.load("res/Play Rect.png"), pos = (640,250),
                                text_input = "PLAY", font = get_font(75), base_color = "#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pygame.image.load("res/Options Rect.png"), pos = (640,400),
                                text_input = "OPTIONS", font = get_font(75), base_color = "#d7fcd4", hovering_color="White") 

        QUIT_BUTTON = Button(image=pygame.image.load("res/Quit Rect.png"), pos = (640,550),
                                text_input = "QUIT", font = get_font(75), base_color = "#d7fcd4", hovering_color="White") 
        
        window.blit(MENU_TEXT,MENU_RECT)

        for button in [PLAY_BUTTON,OPTIONS_BUTTON,QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        


main_menu()
