from functions import *
board = create_board()
turn = 'W'
while True:
    display_board(board)
    board = move_piece(board, turn)
    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
    