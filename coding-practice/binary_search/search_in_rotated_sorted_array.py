"""
Search in Rotated Sorted Array
--------------------------------
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k such that the result is [nums[k], ..., nums[n-1], nums[0], ..., nums[k-1]].

Given the array nums after the possible rotation and an integer target, return the
index of target if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity.

Example:
    Input:  nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input:  nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Input:  nums = [1], target = 0
    Output: -1

Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values in nums are unique
    - nums is an ascending array that is possibly rotated
"""

def search(nums: list[int], target: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([3, 1], 1) == 1
    assert search([5, 1, 3], 3) == 2
    print("All tests passed!")
