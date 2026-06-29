def create_board():
    # Create a board with binary logic
    board = []
    for row in range(8):
        t_list = [] # temporary list
        for col in range(8):
            if (col+row) % 2 == 0:
                t_list.append(0)
            else:
                if row < 3:
                    t_list.append('B') # black piece
                elif row > 4:
                    t_list.append('W') # white piece
                else:
                    t_list.append("_")
        board.append(t_list)
    return board

def display_board(board):
    # Show the board on terminal, it's a temporary function to help on development
    for row in range(8):
        for col in range(8):
            print(board[row][col], end=" ")
        print()

def move_piece(board, turn):
    while True:
        row = int(input("Type the row of the piece that you'd like to move: "))
        col = int(input("Type the col of the piece that you'd like to move: "))
        nrow = int(input("Type the new row to the piece that you'd like to move: "))
        ncol = int(input("Type the new col of the piece that you'd like to move: "))
        if board[row][col] != turn:
            print('Invalid! You need to move some piece and not a white space or a enemy piece.')
        else:
            temp_value = board[row][col]
            board[nrow][ncol] = temp_value
            board[row][col] = "_"
            break
    return board