"""
Coin Change
------------
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If the amount cannot be reached by any combination, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
    Input:  coins = [1,5,11], amount = 15
    Output: 3   (5+5+5 — greedy fails here! 11+1+1+1+1 = 5 coins)

    Correction: coins=[1,5,11], amount=15 → 11+4*1=5 coins, or 3*5=3 coins → answer is 3

    Input:  coins = [1,2,5], amount = 11
    Output: 3   (5+5+1)

    Input:  coins = [2], amount = 3
    Output: -1

    Input:  coins = [1], amount = 0
    Output: 0

Constraints:
    - 1 <= coins.length <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4
"""

def coin_change(coins: list[int], amount: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 2) == 2
    assert coin_change([1, 5, 11], 15) == 3
    print("All tests passed!")
