import pygame
import sys
import random #new addition

pygame.init()

WIDTH, HEIGHT = 900, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]
#Old working code
to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))



pygame.display.update()
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
def add_XO(board, graphical_board):#board, graphical_board, to_move
    global to_move  # Declare to_move as a global variable

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
    return board #, to_move


game_finished = False


def check_win(board):
    winner = None
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                #graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                # SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])


                #new code
                if graphical_board[row][i][0] is not None:
                    position = graphical_board[row][i][1].topleft
                    SCREEN.blit(graphical_board[row][i][0], position)
                # new code
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            for i in range(0, 3):
                #graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                #SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])

                # new code
                if graphical_board[i][col][0] is not None:
                    position = graphical_board[i][col][1].topleft
                    SCREEN.blit(graphical_board[i][col][0], position)
                # new code


            pygame.display.update()
            return winner

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]


        # new code
        if graphical_board[0][0][0] is not None:
            position = graphical_board[0][0][1].topleft
            SCREEN.blit(graphical_board[0][0][0], position)
        if graphical_board[1][1][0] is not None:
            position = graphical_board[1][1][1].topleft
            SCREEN.blit(graphical_board[1][1][0], position)
        if graphical_board[2][2][0] is not None:
            position = graphical_board[2][2][1].topleft
            SCREEN.blit(graphical_board[2][2][0], position)
        # new code


        pygame.display.update()
        return winner

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]


        # new code
        if graphical_board[0][2][0] is not None:
            position = graphical_board[0][2][1].topleft
            SCREEN.blit(graphical_board[0][2][0], position)
        if graphical_board[1][1][0] is not None:
            position = graphical_board[1][1][1].topleft
            SCREEN.blit(graphical_board[1][1][0], position)
        if graphical_board[2][0][0] is not None:
            position = graphical_board[2][0][1].topleft
            SCREEN
        # new code



        pygame.display.update()
        return winner

    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"
def ai_move(board):
    available_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isinstance(board[i][j], int):
                available_moves.append((i, j))

    if available_moves:
        return random.choice(available_moves)
    else:
        return None


def get_ai_move(board):
    # Generate a random move for the AI
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                available_moves.append((i, j))

    # Choose a random available move
    ai_move = random.choice(available_moves)

    return ai_move


####NEW CODE

#num_moves = 0

ai_turn = False

while True:
    to_move = 'X'  # Initialize to_move variable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Increment the number of moves
            board = add_XO(board, graphical_board)






            if game_finished:
                # Reset the number of moves
                #num_moves = 0
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]],
                                   [[None, None], [None, None], [None, None]],
                                   [[None, None], [None, None], [None, None]]]

                game_finished = False
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))


                pygame.display.update()

            if check_win(board) is not None:
                game_finished = True

                # AI's move
                ai_turn = True
            #AI
            if not game_finished and to_move == 'X':
                # AI's move after player's first move
                ai_turn = True
            # Render the updated board and check for a win again
            if check_win(board) is not None:
                game_finished = True

            pygame.display.update()

        # AI's move
        if ai_turn:
            move = get_ai_move(board)
            if move is not None:
                i, j = move
                board[i][j] = 'O'
                #to_move = 'X'
                ai_turn = False
                pygame.display.update()

