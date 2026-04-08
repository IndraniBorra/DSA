"""
Container With Most Water
--------------------------
You are given an integer array `height` of length n. There are n vertical lines drawn
such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water a container can store.

You may not slant the container.

Example:
    Input:  height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input:  height = [1,1]
    Output: 1

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4
"""

def max_area(height: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("All tests passed!")
