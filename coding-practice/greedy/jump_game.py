"""
Jump Game
----------
You are given an integer array nums. You are initially positioned at the first
index, and each element in the array represents your maximum jump length at that position.

Return True if you can reach the last index, or False otherwise.

Example:
    Input:  nums = [2,3,1,1,4]
    Output: True   (jump 1 to index 1, then 3 to last)

    Input:  nums = [3,2,1,0,4]
    Output: False  (always stuck at index 3)

Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5
"""

def can_jump(nums: list[int]) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    assert can_jump([0]) == True
    assert can_jump([1, 0]) == True
    assert can_jump([0, 1]) == False
    assert can_jump([2, 0, 0]) == True
    print("All tests passed!")
