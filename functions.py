def create_board():
    # Create a board with binary logic
    board = []
    for row in range(8):
        t_list = [] # temporary list
        for col in range(8):
            if (col+row) % 2 == 0:
                t_list.append("0")
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

def check_piece(board, row, col):
    if board[row][col] == "WW" or board[row][col] == "BB":
        valid_moviment = 'k' #king
        return valid_moviment
    else:
        valid_moviment = 'c' #checker
        return valid_moviment

def move_piece(board, turn, nrow, ncol, row, col):
    # Function that move the checkers.
    if turn == 'W': nturn = 'B'
    if turn == 'B': nturn = 'W'
    check_answer = check_piece(board, row, col)
    if check_answer == 'k':
        sucess, enemy_positions = move_king(board, turn, nturn, row, col, nrow, ncol)
    else:
        sucess, enemy_positions = move_checker(board, turn, nturn, row, col, nrow, ncol)
    if sucess == False:
        return False, []
    return True, enemy_positions

def move_king(board, turn, nturn, row, col, nrow, ncol):
    # rules of king moviment
    if abs(nrow-row) != abs(ncol-col):
        return False
    if nrow > row:
        step_row = 1
    else:
        step_row = -1
    if ncol > col:
        step_col = 1
    else:
        step_col = -1
    trow = row + step_row #trow and tcol are temporary variables
    tcol = col + step_col
    enemy_positions = []
    valid = True
    while trow != nrow and tcol != ncol:
        if turn in board[trow][tcol]:
            print('Invalid! you can not do that.')
            break
        elif nturn in board[trow][tcol]:
            enemy_positions.append((trow, tcol))
            if len(enemy_positions) > 1:
                print('Invalid! You need to catch only one enemy by step.')
                valid = False
                break
        trow = trow + step_row
        tcol = tcol + step_col
    if valid == True:
        if board[nrow][ncol] != '_':
            return False
        elif len(enemy_positions) == 1:
            enemy_row, enemy_col = enemy_positions[0]
            board[enemy_row][enemy_col] = '_'
        board[nrow][ncol] = board[row][col]
        board[row][col] = '_'
        return True, enemy_positions
    else: 
        return False, []

def move_checker(board, turn, nturn, row, col, nrow, ncol):
    # rules of checker moviment
    enemy_positions = []
    if turn not in board[row][col]:
        return False, []
    elif not ((abs(nrow - row) == 1 and abs(ncol - col) == 1) or (abs(nrow - row) == 2 and abs(ncol - col) == 2)):
        return False, []
    elif ((abs(nrow - row) == 2) and nturn not in board[(nrow + row) // 2][(ncol + col) // 2]):
        return False, []
    elif board[nrow][ncol] != "_":
        return False, [] 
    elif turn == 'B' and (nrow-row) < 0 and board[row][col] == 'B':
        return False, []
    elif turn == 'W' and (nrow-row) > 0 and board[row][col] == 'W':
        return False, []
    else:
        if abs(nrow-row) == 2 and abs(ncol-col) == 2:
            enemy_positions.append(((nrow+row)//2, (ncol+col)//2))
            board[(nrow+row)//2][(ncol+col)//2] = '_'
        temp_value = board[row][col]
        board[nrow][ncol] = temp_value
        board[row][col] = "_"

    return True, enemy_positions

def check_queen(board, nrow, ncol):
    # Check if the moved piece will be promoted to a queen
    if board[nrow][ncol] == 'W' and nrow == 0:
        board[nrow][ncol] = 'WW'
    elif board[nrow][ncol] == 'B' and nrow == 7:
        board[nrow][ncol] = 'BB'
    return board

