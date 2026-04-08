"""
Triangle Numbers (Valid Triangle Number)
-----------------------------------------
Given an integer array nums, return the number of triplets chosen from the
array that can make triangles if we take them as side lengths of a triangle.

A valid triangle requires: a + b > c  (for all permutations of the three sides)

Example:
    Input:  nums = [2,2,3,4]
    Output: 3
    Explanation: Valid triplets are (2,3,4), (2,3,4), (2,2,3)

    Input:  nums = [4,2,3,4]
    Output: 4

Constraints:
    - 1 <= nums.length <= 1000
    - 0 <= nums[i] <= 1000
"""

def triangle_number(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert triangle_number([2, 2, 3, 4]) == 3
    assert triangle_number([4, 2, 3, 4]) == 4
    assert triangle_number([0, 0, 0]) == 0
    assert triangle_number([1, 1, 1, 1]) == 4
    print("All tests passed!")
