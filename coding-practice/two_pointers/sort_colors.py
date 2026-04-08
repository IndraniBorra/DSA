"""
Sort Colors (Dutch National Flag)
-----------------------------------
Given an array nums with n objects colored red, white, or blue, represented
as 0, 1, and 2 respectively, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue.

You must solve this without using the library's sort function.
One-pass algorithm using only constant extra space preferred.

Example:
    Input:  nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

    Input:  nums = [2,0,1]
    Output: [0,1,2]

Constraints:
    - n == nums.length
    - 1 <= n <= 300
    - nums[i] is either 0, 1, or 2
"""

def sort_colors(nums: list[int]) -> None:
    """Modifies nums in-place."""
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    assert a == [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sort_colors(b)
    assert b == [0, 1, 2]

    c = [0]
    sort_colors(c)
    assert c == [0]

    d = [1]
    sort_colors(d)
    assert d == [1]

    print("All tests passed!")
