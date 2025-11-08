#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for r, c in board:
        # eyni sütun
        if col == c:
            return False
        # eyni diaqonal
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(N, board=[], row=0):
    """Backtracking solver"""
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            solve_nqueens(N, board + [[row, col]], row + 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
