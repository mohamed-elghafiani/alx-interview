#!/usr/bin/python3
"""Calculate the pascal triangle"""

def pascal_triangle(n):
    """return the pascal triangle for @n"""
    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        res = [[1], [1, 1]]
        for i in range(3, n + 1):
            row = [1]
            for j in range(len(res[i-2]) - 1):
                row.append(res[i-2][j] + res[i-2][j+1])
            row.append(1)
            res.append(row)

        return res
