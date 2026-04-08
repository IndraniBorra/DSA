"""
Jump Game II
-------------
You are given a 0-indexed array of integers nums of length n. You are initially
positioned at index 0, and each element represents your maximum jump length.

Return the minimum number of jumps to reach the last index. You can always
reach the last index (unlike Jump Game I).

Example:
    Input:  nums = [2,3,1,1,4]
    Output: 2   (jump from 0→1, then 1→4)

    Input:  nums = [2,3,0,1,4]
    Output: 2   (jump from 0→1, then 1→4)

Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 1000
    - It is guaranteed you can reach the last index
"""

def jump(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([1]) == 0
    assert jump([1, 2]) == 1
    assert jump([1, 1, 1, 1]) == 3
    assert jump([3, 2, 1, 0, 4, 1, 1]) == 3
    print("All tests passed!")
