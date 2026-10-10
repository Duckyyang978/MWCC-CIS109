# TIC-TAC-TOE - Lab 05

matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

players = ["O", "X"]
turns = 0
winner = None


def print_board():
    print("\nTIC-TAC-TOE")
    for row in matrix:
        print(" | ".join(row))
    print()


def check_winner():
    # Check horizontal and vertical wins
    for i, row in enumerate(matrix):
        if row[0] == row[1] == row[2] != "-":
            return row[0]

        if matrix[0][i] == matrix[1][i] == matrix[2][i] != "-":
            return matrix[0][i]

    # Check diagonal wins
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-":
        return matrix[0][0]

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
        return matrix[0][2]

    return None


while turns < 9 and winner is None:
    print_board()

    player = players[turns % 2]
    print(f"{player}'s Turn")

    try:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid row or column. Please enter numbers from 1 to 3.")
            input("Hit [enter] to continue.")
            continue

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        input("Hit [enter] to continue.")
        continue

    # Convert user input to list indexes
    row -= 1
    col -= 1

    if matrix[row][col] != "-":
        print(
            f"Someone has already claimed row {row + 1} "
            f"and col {col + 1}!"
        )
        input("Hit [enter] to continue.")
        continue

    matrix[row][col] = player
    turns += 1

    winner = check_winner()


# Game over
print_board()

if winner is not None:
    print(f"{winner} won!")
else:
    print("It's a draw!")

print("Game Over!")
print("Thanks for playing!")