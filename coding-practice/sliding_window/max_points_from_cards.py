"""
Max Points You Can Obtain From Cards
--------------------------------------
There are several cards arranged in a row, and each card has an associated
number of points. In one step, you can take one card from the beginning or
from the end of the row. You have to take exactly k cards.

Return the maximum score you can obtain.

Example:
    Input:  cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12   (take [1,6,5] from right end)

    Input:  cardPoints = [2,2,2], k = 2
    Output: 4

    Input:  cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55

Constraints:
    - 1 <= cardPoints.length <= 10^5
    - 1 <= cardPoints[i] <= 10^4
    - 1 <= k <= cardPoints.length
"""

def max_score(card_points: list[int], k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_score([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert max_score([2, 2, 2], 2) == 4
    assert max_score([9, 7, 7, 9, 7, 7, 9], 7) == 55
    assert max_score([1, 1000, 1], 1) == 1
    print("All tests passed!")
