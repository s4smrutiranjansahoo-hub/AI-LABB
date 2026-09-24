
# Function to print the chessboard.

def print_board(board):
    for row in board:
        print(" ".join(row))


# Function to check if a queen can be placed safely.

def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solved(board, row):

    # All 8 queens have been placed
    if row == 8:
        return True

    # Try every column in the current row
    for col in range(8):

        if is_safe(board, row, col):

            # Place queen
            board[row][col] = 'Q'

            # Recursively place queen in next row
            if solved(board, row + 1):
                return True

            # Backtrack
            board[row][col] = '.'

    return False


# Main Program
board = [['.' for _ in range(8)] for _ in range(8)]

if solved(board, 0):
    print("\nSolution for 8-Queens Problem:\n")
    print_board(board)
else:
    print("No Solution Exists.")
