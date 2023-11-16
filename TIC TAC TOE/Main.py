import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Fonts
font = pygame.font.Font(None, 100)

def draw_board():
    # Draw horizontal lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    # Draw vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_markers():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 4
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 4
                pygame.draw.line(screen, RED, (x_pos, y_pos), (x_pos + SQUARE_SIZE // 2, y_pos + SQUARE_SIZE // 2), LINE_WIDTH)
                pygame.draw.line(screen, RED, (x_pos, y_pos + SQUARE_SIZE // 2), (x_pos + SQUARE_SIZE // 2, y_pos), LINE_WIDTH)
            elif board[row][col] == 'O':
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 4
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 4
                pygame.draw.circle(screen, BLUE, (x_pos + SQUARE_SIZE // 4, y_pos + SQUARE_SIZE // 4), SQUARE_SIZE // 4, LINE_WIDTH)

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(BOARD_SIZE):
        # Check rows and columns
        if all(board[i][j] == 'X' for j in range(BOARD_SIZE)) or all(board[j][i] == 'X' for j in range(BOARD_SIZE)):
            return 'X'
        elif all(board[i][j] == 'O' for j in range(BOARD_SIZE)) or all(board[j][i] == 'O' for j in range(BOARD_SIZE)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 'X' for i in range(BOARD_SIZE)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 'O' for i in range(BOARD_SIZE)):
        return 'O'

    return None

def is_board_full():
    return all(board[i][j] != '' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

def main():
    turn = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if board[row][col] == '':
                    board[row][col] = turn

                    winner = check_winner()
                    if winner:
                        print(f'Player {winner} wins!')
                        game_over = True
                    elif is_board_full():
                        print('It\'s a tie!')
                        game_over = True
                    else:
                        turn = 'O' if turn == 'X' else 'X'

        screen.fill(WHITE)
        draw_board()
        draw_markers()

        pygame.display.flip()

if __name__ == "__main__":
    main()
