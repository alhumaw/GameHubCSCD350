import pygame
import sys
from options import options

# Initialize pygame
pygame.init()


# Constants
WIDTH, HEIGHT = 1280, 720
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = min(WIDTH // BOARD_SIZE, HEIGHT // BOARD_SIZE)

# Colors
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


def draw_lines():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)


def draw_symbols(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            symbol = board[row][col]
            if symbol == "X":
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 2
                pygame.draw.line(screen, X_COLOR, (x_pos - SQUARE_SIZE // 4, y_pos - SQUARE_SIZE // 4),
                                 (x_pos + SQUARE_SIZE // 4, y_pos + SQUARE_SIZE // 4), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, (x_pos + SQUARE_SIZE // 4, y_pos - SQUARE_SIZE // 4),
                                 (x_pos - SQUARE_SIZE // 4, y_pos + SQUARE_SIZE // 4), LINE_WIDTH)
            elif symbol == "O":
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 2
                pygame.draw.circle(screen, O_COLOR, (x_pos, y_pos), SQUARE_SIZE // 4, LINE_WIDTH)


def check_win(board):
    # Check rows
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    # Check columns
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # Check for draw
    if all(all(cell is not None for cell in row) for row in board):
        return "DRAW"

    return None


def start_tictactoe(window):
    # Create the game board
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    pause = False
    # Current player
    current_player = "X"

    # Game state
    game_over = False
    winner = None

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pause = not pause
                    if pause:
                        state = options(window, pause)
                        if not state:
                            print()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if winner is None:
                    mouse_pos = pygame.mouse.get_pos()
                    col = mouse_pos[0] // SQUARE_SIZE
                    row = mouse_pos[1] // SQUARE_SIZE

                    if board[row][col] is None:
                        board[row][col] = current_player
                        current_player = "O" if current_player == "X" else "X"

                winner = check_win(board)

        screen.fill(BG_COLOR)
        draw_lines()
        draw_symbols(board)
        pygame.display.flip()

        if winner is not None:
            game_over = True

    # Game ended, display the winner or draw message
    if winner == "DRAW":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")
