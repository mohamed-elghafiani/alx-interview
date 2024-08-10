#!/usr/bin/python3
"""alx interview
   Island perimeter problem solution module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): The grid representing the island,
    where 1 is land and 0 is water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:
                    perimeter -= 1

    return perimeter
