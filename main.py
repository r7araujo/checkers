import sys, pygame
from functions import *

pygame.init()
square_size = 80
width, height = 640, 640
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('The checkers game')

# colors
beige = (240, 217, 181)
brown = (181, 136, 99)
white = (255, 255, 255)
black = (50, 50, 50)
red = (255, 0, 0)

board = create_board()
clock = pygame.time.Clock()

running = True
selected = None
turn = 'W'
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // square_size
            row = pos[1] // square_size
            if turn in board[row][col]:
                selected = (row, col)
            
            elif selected != None: #the second click is to move the piece
                nrow = row
                ncol = col
                row, col = selected
                sucess, enemy_positions = move_piece(board, turn, nrow, ncol, row, col)
                if not sucess:
                    pygame.draw.rect(screen, red, (ncol * square_size, nrow * square_size, square_size, square_size))
                    pygame.display.flip()
                    pygame.time.delay(200)
                else:
                    board = check_queen(board, nrow, ncol)
                    switch = check_sequence(board, turn, nrow, ncol)
                    if switch == True:        
                        if turn == 'W': #switch the turn
                            turn = 'B'
                        else:
                            turn = 'W'
            

    screen.fill(beige)
    # draw the board
    for r in range(8):
        for c in range(8):
            if (r+c) % 2 == 1:
                pygame.draw.rect(screen, brown, (c*square_size, r*square_size, square_size, square_size))
    # draw the pieces
    for r in range(8):
        for c in range(8):
            center_x = c * square_size + square_size // 2
            center_y = r * square_size + square_size // 2
            radius = square_size // 2 - 10
            if board[r][c] == 'B':
                pygame.draw.circle(screen,black, (center_x, center_y), radius)
            elif board[r][c] == 'BB':
                pygame.draw.circle(screen,black, (center_x, center_y), radius)
                pygame.draw.circle(screen,red, (center_x, center_y), radius // 3)
            elif board[r][c] == 'W':
                pygame.draw.circle(screen, white, (center_x, center_y), radius)
            elif board[r][c] == 'WW':
                pygame.draw.circle(screen, white, (center_x, center_y), radius)
                pygame.draw.circle(screen,red, (center_x, center_y), radius // 3)
    if selected is not None:
        r, c = selected
        pygame.draw.rect(screen, red, (c*square_size, r*square_size, square_size, square_size), 4)

    pygame.display.flip()
            








turn = 'W'
while True:
    display_board(board)
    board, nrow, ncol = move_piece(board, turn)
    board = check_queen(board, nrow, ncol)
    switch = check_sequence(board, turn, nrow, ncol)
    if switch == True:        
        if turn == 'W': #switch the turn
            turn = 'B'
        else:
            turn = 'W'
