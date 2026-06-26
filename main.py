from solver import solve_visual
import tkinter as tk

root = tk.Tk()
root.title("Sudoku Solver & Algorithm Visualizer")
root.geometry("600x650")
root.resizable(False, False)

# This list will store all 81 boxes
cells = []

board_frame = tk.Frame(root)
board_frame.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)


def validate_input(value):
    if value == "":
        return True
    return len(value) == 1 and value in "123456789"


vcmd = (root.register(validate_input), "%P")

for row in range(9):
    current_row = []

    for col in range(9):
        entry = tk.Entry(
            board_frame,
            width=2,
            font=("Arial", 20),
            justify="center",
            validate="key",
            validatecommand=vcmd
        )

        entry.grid(
            row=row,
            column=col,
            padx=(4 if col % 3 == 0 else 1,
                  4 if col == 8 else (4 if (col + 1) % 3 == 0 else 1)),
            pady=(4 if row % 3 == 0 else 1,
                  4 if row == 8 else (4 if (row + 1) % 3 == 0 else 1))
        )

        current_row.append(entry)

    cells.append(current_row)

def get_board():

    board = []

    for row in range(9):

        current_row = []

        for col in range(9):

            value = cells[row][col].get()

            if value == "":
                current_row.append(0)
            else:
                current_row.append(int(value))

        board.append(current_row)

    return board

def display_board(board):

    for row in range(9):
        for col in range(9):

            cells[row][col].delete(0, tk.END)

            if board[row][col] != 0:
                cells[row][col].insert(0, str(board[row][col]))

def update_gui(board):

    display_board(board)

    root.update()

def clear_board():

    for row in range(9):
        for col in range(9):
            cells[row][col].delete(0, tk.END)


def solve_board():

    board = get_board()

    solve_visual(board, update_gui)


tk.Button(
    button_frame,
    text="Solve",
    width=12,
    font=("Arial", 12),
    command=solve_board
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    font=("Arial", 12),
    command=clear_board
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Validate",
    width=12,
    font=("Arial", 12)
).grid(row=0, column=2, padx=10)

root.mainloop()