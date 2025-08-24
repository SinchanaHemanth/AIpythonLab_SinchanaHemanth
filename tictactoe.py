def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  
    moves = 0

    print("Tic Tac Toe positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")

    while moves < 9:
        print_board(board)
        try:
            pos = int(input(f"Player {current_player}, enter your move (1-9): "))
            if pos < 1 or pos > 9:
                print("Invalid position! Choose between 1 and 9.")
                continue

            row, col = divmod(pos - 1, 3)

            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue

            board[row][col] = current_player
            moves += 1

            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "X":
                    print("🎉 Player 1 (X) wins! Cost: +1 | Player 2 (O): -1")
                else:
                    print("🎉 Player 2 (O) wins! Cost: +1 | Player 1 (X): -1")
                return

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number between 1 and 9.")

    print_board(board)
    print("🤝 It's a Draw! Cost: 0")


play_tic_tac_toe()
