"""
Apple Harvest (Minimum Eating Speed / Koko Eating Bananas style)
-----------------------------------------------------------------
You have n piles of apples and h hours to eat all of them. Each hour you can
eat at most k apples from a single pile. You want to finish all piles within
h hours. Find the minimum integer k such that you can eat all the apples.

(This is the classic "Koko Eating Bananas" / binary search on answer pattern.)

Example:
    Input:  piles = [3,6,7,11], h = 8
    Output: 4

    Input:  piles = [30,11,23,4,20], h = 5
    Output: 30

    Input:  piles = [30,11,23,4,20], h = 6
    Output: 23

Constraints:
    - 1 <= piles.length <= 10^4
    - piles.length <= h <= 10^9
    - 1 <= piles[i] <= 10^9
"""
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1, 1, 1, 1], 4) == 1
    print("All tests passed!")
