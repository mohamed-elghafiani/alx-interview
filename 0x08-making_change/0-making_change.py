#!/usr/bin/python3
"""
This module contains the makeChange function that calculates the fewest number
of coins needed to meet a given total.
"""

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
    
    # Initialize dp array with infinity, representing the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0
    
    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (total cannot be formed)
    return dp[total] if dp[total] != float('inf') else -1

