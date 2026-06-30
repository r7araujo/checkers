from functions import *
board = create_board()
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
