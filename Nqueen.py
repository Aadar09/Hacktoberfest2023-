def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Convert the board to a solution
        solution = []
        for i in range(n):
            row_str = ""
            for j in range(n):
                if board[i][j] == 1:
                    row_str += "Q"
                else:
                    row_str += "."
            solution.append(row_str)
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    n = 8  # Change this to the desired board size (e.g., n = 8 for 8-queens)
    solutions = solve_n_queens(n)
    print(f"Solutions for {n}-queens problem:")
    print_solutions(solutions)
