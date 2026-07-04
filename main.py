import pygame, pygame_gui, sys
from functions import *
from config import *

pygame.init()
screen = pygame.display.set_mode((width + 160, height))
ui_manager = pygame_gui.UIManager((width+160, height))
pygame.display.set_caption('The checkers game')
board = create_board()
clock = pygame.time.Clock()
play_again_button = None
running = True
selected = None
turn = 'W'
mandatory_move = []
necessary_sequence = []
black_points = white_points = 0
while running:
    clock.tick(60)
    mandatory_move = get_mandatory_captures(board, turn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // square_size
            row = pos[1] // square_size
            if col >= 8 or row >= 8: # avoid clicks out of the board
                continue
            if turn in board[row][col]:
                selected = (row, col)
            
            elif selected != None: #the second click is to move the piece
                nrow, ncol = row, col
                row, col = selected
                if len(mandatory_move) > 0:
                    if (row, col, nrow, ncol) in mandatory_move:
                        sucess, enemy_positions = move_piece(board, turn, nrow, ncol, row, col)
                        if turn == 'W': white_points = white_points + 1
                        else: black_points = black_points + 1
                        board = check_queen(board, nrow, ncol)
                        sequence = check_sequence(board, turn, nrow, ncol, row, col, enemy_positions)
                        if sequence == False:   
                            selected = None
                            if turn == 'W': #switch the turn
                                turn = 'B'
                            else:
                                turn = 'W'
                        else: # sequence True
                            selected = (nrow, ncol)
                            mandatory_move = [m for m in get_mandatory_captures(board, turn) if m[0] == nrow and m[1] == ncol]
                    else:
                        pygame.draw.rect(screen, red, (col * square_size, row * square_size, square_size, square_size))
                        pygame.draw.rect(screen, red, (ncol * square_size, nrow * square_size, square_size, square_size))
                        pygame.display.flip()
                        pygame.time.delay(200)    
                else:
                    sucess, enemy_positions = move_piece(board, turn, nrow, ncol, row, col)
                    if not sucess:
                        pygame.draw.rect(screen, red, (ncol * square_size, nrow * square_size, square_size, square_size))
                        pygame.display.flip()
                        pygame.time.delay(200)
                    else:
                        board = check_queen(board, nrow, ncol)
                        sequence = check_sequence(board, turn, nrow, ncol, row, col, enemy_positions)
                        if sequence == False:  
                            selected = None      
                            if turn == 'W': #switch the turn
                                turn = 'B'
                            else:
                                turn = 'W'
                        else:
                            selected = (nrow,ncol)
                            mandatory_move = [m for m in get_mandatory_captures(board, turn) if m[0] == nrow and m[1] == ncol]
                

    screen.fill(beige)
    pygame.draw.rect(screen, (30, 30, 30), (640, 0, 160, 640))
    if turn == 'W':
        color_turn = (255, 255, 255)
        board_color = (100, 100, 100)
    else:
        color_turn = (0, 0, 0)
        board_color = (200, 200, 200)
    pygame.draw.circle(screen, color_turn, (720, 120), 40)
    pygame.draw.circle(screen, board_color, (720, 120), 40, 3)
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
    if black_points == 12: winner = 'B'
    elif white_points == 12: winner = 'W'


    pygame.display.flip()