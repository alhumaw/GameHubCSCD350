import pygame
import sys
import random
from options import options
from pygame import mixer
from options import options
import assets




def start_tictactoe(window):
    pygame.init()
    mixer.init()
    width = 1280
    height = 720

    bound_width = 1000
    bound_height = 700

    retx = int((width - bound_width) / 2)
    rety = int((height - bound_height) / 2)
    pygame.init()

    SCREEN = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tic Tac Toe!")

    BOARD = pygame.image.load("res/Board.png")
    X_IMG = pygame.image.load("res/X.png")
    O_IMG = pygame.image.load("res/O.png")

    BG_COLOR = (214, 201, 227)

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    graphical_board = [[[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]

    to_move = 'X'

    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64, 64))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board, to_move = add_XO(board, graphical_board, to_move)
                game_finished = False
                if game_finished:
                    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                    graphical_board = [[[None, None], [None, None], [None, None]],
                                       [[None, None], [None, None], [None, None]],
                                       [[None, None], [None, None], [None, None]]]

                    to_move = 'X'

                    SCREEN.fill(BG_COLOR)
                    SCREEN.blit(BOARD, (64, 64))

                    #game_finished = False

                    pygame.display.update()

                if check_win(board) is not None:
                    game_finished = True
                pygame.display.update()
                # Set the desired FPS
                #clock.tick(60)
width = 600#1280
height = 600#720
X_IMG = pygame.image.load("res/X.png")
O_IMG = pygame.image.load("res/O.png")

SCREEN = pygame.display.set_mode((width, height))

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]

to_move = 'X'

#NEW CODE
def draw_game_board(window, game_board):
    # Define the dimensions and positions of the game board cells
    cell_width = 200
    cell_height = 200
    cell_margin = 10

    # Clear the window
    window.fill((255, 255, 255))

    # Iterate over the game board and draw the symbols in each cell
    for row in range(3):
        for col in range(3):
            x = col * (cell_width + cell_margin)
            y = row * (cell_height + cell_margin)

            cell_rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(window, (0, 0, 0), cell_rect)

            symbol = game_board[row][col]
            if symbol is not None:
                symbol_text = get_font(150).render(symbol, True, (0, 0, 0))
                symbol_rect = symbol_text.get_rect(center=cell_rect.center)
                window.blit(symbol_text, symbol_rect)

    pygame.display.update()

def check_winner(game_board):
    # Check rows
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] is not None:
            return game_board[row][0]

    # Check columns
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] is not None:
            return game_board[0][col]

    # Check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] is not None:
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] is not None:
        return game_board[0][2]

    # No winner
    return None

def is_board_full(game_board):
    # Check if the game board is full (no empty cells)
    for row in range(3):
        for col in range(3):
            if game_board[row][col] is None:
                return False
    return True

#NEW CODE




def render_board(board, X_IMG, O_IMG):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                #Create an X image and rect
                graphical_board[i][j][0] = X_IMG
                graphical_board[i][j][1] = X_IMG.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                # Create a Y image and rect
                graphical_board[i][j][0] = O_IMG
                graphical_board[i][j][1] = O_IMG.get_rect(center=(j * 300 + 150, i * 300 + 150))
def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos() #returns tuple/coordinates of mouse(x=100,y=200,(100,200))
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1] / 835 * 2
    if board[round(converted_y)][round(converted_x)] !='O' and board[round(converted_y)][round(converted_x)] !='X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    return board, to_move


game_finished = False


def check_win(board):
    winner = None
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"res/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"res/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"res/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        return winner

    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"


        # Create the game window
        window = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Tic Tac Toe!")

        # Call the start_tictactoe function to start the game
        start_tictactoe(window)
             
  



           
