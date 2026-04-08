"""
Trapping Rain Water
--------------------
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example:
    Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Input:  height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    - n == height.length
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5
"""

def trap(height: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([3, 0, 2, 0, 4]) == 7
    assert trap([1, 0, 1]) == 1
    assert trap([1]) == 0
    print("All tests passed!")
