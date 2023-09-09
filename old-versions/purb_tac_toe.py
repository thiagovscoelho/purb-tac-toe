def display_board(board):
    """Display the board dynamically, creating labels for empty spaces."""
    print("yummi:")
    label_count = 1
    for row in board:
        row_display = []
        for cell in row:
            if cell == " ":
                if label_count <= 9:
                    row_display.append(str(label_count))
                else:
                    row_display.append(chr(64 + (label_count - 9)))
                label_count += 1
            else:
                row_display.append(cell)
        print(" ".join(row_display))

def make_move(board, position, symbol):
    """Make a move on the board, updating the internal matrix."""
    empty_positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                empty_positions.append((i, j))
    x, y = empty_positions[position - 1]
    board[x][y] = symbol

def expand_board(board, position):
    """Expand the board depending on the chosen position."""
    if position == 1:
        board.insert(0, [" ", " ", " "])
        for row in board:
            row.insert(0, " ")
    elif position == 3:
        board.insert(0, [" ", " ", " "])
        for row in board:
            row.append(" ")
    elif position == 6:
        board.append([" ", " ", " "])
        for row in board:
            row.insert(0, " ")
    elif position == 8:
        board.append([" ", " ", " "])
        for row in board:
            row.append(" ")
    elif position == 2:
        board.insert(0, [" ", " ", " "])
    elif position == 4:
        for row in board:
            row.insert(0, " ")
    elif position == 5:
        for row in board:
            row.append(" ")
    elif position == 7:
        board.append([" ", " ", " "])

# Initialize the internal 3x3 board with only the center filled
initial_board = [
    [" ", " ", " "],
    [" ", "x", " "],
    [" ", " ", " "]
]

# Display the initial board with labels for stage 1
display_board(initial_board)
print("purb (enter move 1–8):")

# Uncomment these lines to play the game interactively
# player_input = int(input("purb (enter move 1–8): "))
# make_move(initial_board, player_input, 'o')
# expand_board(initial_board, player_input)
# display_board(initial_board)
