from Button import Button
import pygame,sys


# modular ability to change the size of the font


def menu():
    from main import main_menu
    main_menu()


def get_font(size):
    return pygame.font.Font("res/fonts/chary___.ttf", size)

def options(window,pause):
    while True:
        # constantly record the mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # white overlay
        #window.fill("white")
        # text rendering
        OPTIONS_TEXT = get_font(45).render("PAUSED", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        window.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # back button
        SETTINGS = Button(image=None, pos=(640,560), text_input="SETTINGS", font = get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        RETURN_MENU = Button(image=None, pos=(640,360),text_input="RETURN TO MENU", font=get_font(75), base_color ="White", hovering_color="Green")
        # changing colors on hover
        RETURN_MENU.changeColor(OPTIONS_MOUSE_POS)
        RETURN_MENU.update(window)
        SETTINGS.changeColor(OPTIONS_MOUSE_POS)
        SETTINGS.update(window)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SETTINGS.checkForInput(OPTIONS_MOUSE_POS):
                    print("Settings")
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pause = not pause
                    return
                if RETURN_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    menu()
        pygame.display.update()

