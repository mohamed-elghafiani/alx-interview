from collections import deque

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to be met with the fewest number of coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize the BFS queue
    queue = deque([(0, 0)])  # (current amount, number of coins)
    visited = set()  # To keep track of visited amounts

    while queue:
        current_amount, num_coins = queue.popleft()

        # Try every coin and add the new amount to the queue if not visited
        for coin in coins:
            new_amount = current_amount + coin

            if new_amount == total:
                return num_coins + 1  # Found the solution
            elif new_amount < total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    # If we exhaust the queue without finding the solution
    return -1
