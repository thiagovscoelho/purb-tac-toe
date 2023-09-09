import random

def display_board(board, player_name, full_display=True):
    """Display the board dynamically, creating labels for empty spaces."""
    print(f"{player_name}:")
    label_count = 1
    for row in board:
        row_display = []
        for cell in row:
            if cell == " ":
                if full_display:
                    if label_count <= 9:
                        row_display.append(str(label_count))
                    else:
                        row_display.append(chr(64 + (label_count - 9)))
                else:
                    row_display.append(" ")
                label_count += 1
            else:
                row_display.append(cell)
        if any(cell != " " for cell in row) or full_display:
            print(" ".join(row_display))

# ... rest of the code remains the same

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
        if check_win(initial_board, 'o'):
            display_board(initial_board, 'purb', full_display=False)
            print("purb wins!")
            break
        elif check_tie(initial_board):
            display_board(initial_board, 'purb', full_display=False)
            print("cat\'s game!")
            break
        display_board(initial_board, 'purb', full_display=False)

        # Computer's move
        computer_move(initial_board, 'x')
        expand_board(initial_board)
        contract_board(initial_board)
        if check_win(initial_board, 'x'):
            display_board(initial_board, 'yummi', full_display=True)
            print("yummi wins!")
            break
        elif check_tie(initial_board):
            display_board(initial_board, 'yummi', full_display=True)
            print("cat\'s game!")
            break
        display_board(initial_board, 'yummi', full_display=True)

if __name__ == "__main__":
    main()
