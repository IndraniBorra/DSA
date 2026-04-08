"""
Largest Rectangle in Histogram
--------------------------------
Given an array of integers heights representing the histogram's bar heights
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.

Example:
    Input:  heights = [2,1,5,6,2,3]
    Output: 10   (rectangle with height 5, width 2: bars at index 2 and 3)

    Input:  heights = [2,4]
    Output: 4

Constraints:
    - 1 <= heights.length <= 10^5
    - 0 <= heights[i] <= 10^4
"""

def largest_rectangle_area(heights: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largest_rectangle_area([0, 0]) == 0
    print("All tests passed!")
