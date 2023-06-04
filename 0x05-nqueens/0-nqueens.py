#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


solutions = []
"""The list of possible solutions to the N queens prob.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""


def get_input():
    """Retrieves and validates this program's arg.
    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of 2 queens are in an attacking mode.
    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if pos0[0] == pos1[0] or pos0[1] == pos1[1] or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]):
        return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens prob.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions, n
    if row == n:
        tmp0 = group.copy()
        if not any(is_attacking(tmp0[i], tmp0[j]) for i in range(n - 1) for j in range(i + 1, n)):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            group.append(pos[a].copy())
            if not any(is_attacking(pos[a], group[i]) for i in range(row)):
                build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Gets the solution for the given chessboard size.
    """
    global pos, n
    pos = [[x // n, x % n] for x in range(n ** 2)]
    group = []
    build_solution(0, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
