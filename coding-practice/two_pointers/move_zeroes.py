"""
Move Zeroes
-----------
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:
    Input:  nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Input:  nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
"""

def move_zeroes(nums: list[int]) -> None:
    """Modifies nums in-place."""
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    assert a == [1, 3, 12, 0, 0]

    b = [0]
    move_zeroes(b)
    assert b == [0]

    c = [1, 0, 0, 2, 3]
    move_zeroes(c)
    assert c == [1, 2, 3, 0, 0]

    d = [1, 2, 3]
    move_zeroes(d)
    assert d == [1, 2, 3]

    print("All tests passed!")
