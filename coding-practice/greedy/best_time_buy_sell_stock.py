"""
Best Time to Buy and Sell Stock
---------------------------------
You are given an array prices where prices[i] is the price of a given stock on
the i-th day. You want to maximize profit by choosing a single day to buy and
a different day in the future to sell.

Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Example:
    Input:  prices = [7,1,5,3,6,4]
    Output: 5   (buy at 1, sell at 6)

    Input:  prices = [7,6,4,3,1]
    Output: 0   (prices only go down)

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
"""

def max_profit(prices: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 1, 2, 0, 1]) == 1
    assert max_profit([1]) == 0
    print("All tests passed!")
