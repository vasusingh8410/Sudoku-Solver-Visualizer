import time
def find_empty(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:
                return (row, col)

    return None

def is_valid(board, num, pos):

    # Check row
    for col in range(9):
        if board[pos[0]][col] == num and col != pos[1]:
            return False

    # Check column
    for row in range(9):
        if board[row][pos[1]] == num and row != pos[0]:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False

    return True



def solve(board):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, num, (row, col)):

            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def solve_visual(board, update_gui):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, num, (row, col)):

            board[row][col] = num

            update_gui(board)

            time.sleep(0.001)

            if solve_visual(board, update_gui):
                return True

            board[row][col] = 0

            update_gui(board)

            time.sleep(0.001)

    return False
