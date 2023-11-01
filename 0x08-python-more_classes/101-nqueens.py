#!/usr/bin/python3
"""
resolves the N-Queen puzzle using backtracking
"""


from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column(board=[]):
    """Adds a column of zeroes to the right of any board
    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets "queen," or 1, to coordinates given in board."""
    board[row][col] = 1


def new_queen(board, row, col):
    """checks that for a new queen placed in the rightmost column"""
    r = row
    c = col

    for i in range(1, N):
        if (c - i) >= 0:
            if (r - i) >= 0:
                if board[r - i][c - i]:
                    return False
            if board[r][c - i]:
                return False
            if (r + i) < N:
                if board[r + i][c - i]:
                    return False
    return True


def formated_coordinatr(cand):
    """Converts a board (matrir of 1 and 0) into a series of row/column
    """
    result = []
    for r, attempt in enumerate(cand):
        result.append([])
        for i, row in enumerate(attempt):
            result[r].append([])
            for j, col in enumerate(row):
                if col:
                    result[r][i].append(i)
                    result[r][i].append(j)
    return result


cand = []
cand.append(board_column())

for col in range(N):
    new_cand = []
    for matrix in cand:
        for row in range(N):
            if new_queen(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column(temp)
                new_cand.append(temp)
    cand = new_cand

for element in formated_coordinatr(cand):
    print(element)
