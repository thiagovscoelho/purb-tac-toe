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

def check_win(board, symbol):
    """Check for a win condition."""
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(row[col] == symbol for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(len(board))):
        return True
    if all(board[i][len(board) - 1 - i] == symbol for i in range(len(board))):
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
        display_board(initial_board, 'purb')
        if check_win(initial_board, 'o'):
            print("purb wins!")
            break

        # Computer's move
        computer_move(initial_board, 'x')
        expand_board(initial_board)
        display_board(initial_board, 'yummi')
        if check_win(initial_board, 'x'):
            print("yummi wins!")
            break

if __name__ == "__main__":
    main()
