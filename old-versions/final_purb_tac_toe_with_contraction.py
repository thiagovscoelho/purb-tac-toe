import random

def display_board(board, player_name):
    """Display the board dynamically, creating labels for empty spaces."""
    print(f"{player_name}:")
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

def computer_move(board, symbol):
    """Make a random move for the computer."""
    empty_positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                empty_positions.append((i, j))
    x, y = random.choice(empty_positions)
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

def contract_board(board):
    """Contract the board by removing illegal rows and columns."""
    # Identify rows with played cells
    played_rows = [i for i, row in enumerate(board) if any(cell != " " for cell in row)]
    
    # Identify columns with played cells
    played_cols = [j for j in range(len(board[0])) if any(row[j] != " " for row in board)]
    
    # Contract rows if needed
    if len(played_rows) > 0:
        min_row = min(played_rows)
        max_row = max(played_rows)
        if max_row - min_row + 1 == 3:
            board[:] = board[min_row:max_row+1]
    
    # Contract columns if needed
    if len(played_cols) > 0:
        min_col = min(played_cols)
        max_col = max(played_cols)
        if max_col - min_col + 1 == 3:
            for row in board:
                del row[:min_col]
                del row[3:]
            
def check_win(board, symbol):
    """Check for a win condition."""
    n = len(board)
    m = len(board[0])

    # Check rows
    for i in range(n):
        for j in range(m - 2):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == symbol:
                return True

    # Check columns
    for j in range(m):
        for i in range(n - 2):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == symbol:
                return True

    # Check diagonals from top-left to bottom-right
    for i in range(n - 2):
        for j in range(m - 2):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == symbol:
                return True

    # Check diagonals from top-right to bottom-left
    for i in range(n - 2):
        for j in range(2, m):
            if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == symbol:
                return True

    return False

def parse_input(input_str):
    """Parse the input to handle alphanumeric characters."""
    if input_str.isdigit():
        return int(input_str)
    else:
        return ord(input_str.upper()) - 64 + 9

def main():
    # Initialize the internal 3x3 board with only the center filled
    initial_board = [
        [" ", " ", " "],
        [" ", "x", " "],
        [" ", " ", " "]
    ]

    # Display the initial board with labels for stage 1
    display_board(initial_board, 'yummi')

    while True:
        # Player's move
        player_input = input("purb (enter your move): ")
        position = parse_input(player_input)
        make_move(initial_board, position, 'o')
        expand_board(initial_board)
        contract_board(initial_board)
        display_board(initial_board, 'purb')
        if check_win(initial_board, 'o'):
            print("purb wins!")
            break

        # Computer's move
        computer_move(initial_board, 'x')
        expand_board(initial_board)
        contract_board(initial_board)
        display_board(initial_board, 'yummi')
        if check_win(initial_board, 'x'):
            print("yummi wins!")
            break

if __name__ == "__main__":
    main()
