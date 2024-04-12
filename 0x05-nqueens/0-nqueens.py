#!/usr/bin/python3
"""ALX interview questions
   NQueens module
"""
import sys


def solveNQueens(n):
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def is_valid_state(state, n):
    return len(state) == n


def get_candidate(state, n):
    if not state:
        return range(n)

    # find next available position
    position = len(state)
    candidates = set(range(n))
    # remove bad candidates
    for row, col in enumerate(state):
        # discard col index if occupied by a queen
        candidates.discard(col)

        dist = position - row
        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_str(state, n)
        solutions.append(state_string)
        return

    for candidate in get_candidate(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def state_to_str(state, n):
    ret = []
    for i, s in enumerate(state):
        ret.append([i, s])
    return ret


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    else:
        solutions = solveNQueens(n)
        for sol in solutions:
            print(sol)
