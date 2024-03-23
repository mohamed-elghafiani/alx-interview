#!/usr/bin/python3
"""alx-interview
   Task: Minimum Operations
"""


def find_num_op(n, text, op, paste, nop, solutions):
    """Find the number of operations possible"""
    if len(text) >= n:
        solutions.append((text, nop))
        return (text, nop)
    solutions = solutions
    if op == 'P':
        text += paste
        nop += 1

        find_num_op(n, text, 'P', paste, nop, solutions)
        find_num_op(n, text, 'CP', paste, nop, solutions)

    elif op == 'CP':
        paste = text
        text += paste
        nop += 2

        find_num_op(n, text, 'P', paste, nop, solutions)
        find_num_op(n, text, 'CP', paste, nop, solutions)
   
    return solutions


def minOperations(n):
    """Find minimum operations needed to arrive at n * 'H' """
    if n > 0:
        solutions = find_num_op(n, text='H', op='CP', paste='', nop=0, solutions=[])
        finals = list(filter(lambda item: len(item[0]) == n, solutions))
        if finals:
            best = min(finals, key=lambda item: item[1])
            return best[1]
        else:
            return 0
    else:
         print('n should be > 0')
