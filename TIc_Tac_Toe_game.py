import random

# Function to display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if someone won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row check
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column check
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# AI move (simple: random available spot)
def ai_move(board):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_spots)

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user = "X"
    ai = "O"

    while True:
        print_board(board)

        # User move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Spot already taken, try again!")
            continue
        board[row][col] = user

        if check_winner(board, user):
            print_board(board)
            print("🎉 You win!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI move
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = ai
        print(f"AI chose: {ai_row}, {ai_col}")

        if check_winner(board, ai):
            print_board(board)
            print("💻 AI wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

# Call the main game loop
play_game()
