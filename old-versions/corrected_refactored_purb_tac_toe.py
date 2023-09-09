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

def expand_board(board):
    """Expand the board to ensure that there is at least one empty row or column around the played spaces."""
    if any(cell != " " for cell in board[0]):
        board.insert(0, [" " for _ in range(len(board[0]))])
    if any(cell != " " for cell in board[-1]):
        board.append([" " for _ in range(len(board[0]))])
    if any(row[0] != " " for row in board):
        for row in board:
            row.insert(0, " ")
    if any(row[-1] != " " for row in board):
        for row in board:
            row.append(" ")

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
# expand_board(initial_board)
# display_board(initial_board)
