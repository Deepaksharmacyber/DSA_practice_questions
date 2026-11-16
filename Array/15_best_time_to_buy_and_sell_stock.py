"""
LeetCode 121: Best Time to Buy and Sell Stock

Problem:
    You are given an array of stock prices where prices[i] is the
    price of the stock on the ith day.

    Choose one day to buy and a later day to sell to maximize profit.
    Return the maximum profit. If no profit is possible, return 0.

LeetCode:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
    Track the minimum price seen so far and calculate the profit
    possible by selling at the current price.

    For each price:
        1. Update the minimum price if the current price is lower.
        2. Calculate the profit from selling at the current price.
        3. Keep track of the maximum profit found.

Complexity:
    Time:  O(n)
    Space: O(1)
"""


def max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit from one stock transaction.

    Args:
        prices: List of stock prices by day.

    Returns:
        The maximum possible profit.
    """

    if not prices:
        return 0

    min_price = prices[0]
    max_profit_value = 0

    for price in prices[1:]:
        # Update the lowest buying price seen so far.
        if price < min_price:
            min_price = price

        # Calculate profit if we sell at the current price.
        profit = price - min_price

        # Update the maximum profit.
        if profit > max_profit_value:
            max_profit_value = profit

    return max_profit_value


if __name__ == "__main__":
    prices = [2, 5, 4, 1, 7, 9]

    result = max_profit(prices)

    print(result)

    # Output:
    # 8