"""
Partition Equal Subset Sum
---------------------------
Given an integer array nums, return True if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal,
or False otherwise.

Example:
    Input:  nums = [1,5,11,5]
    Output: True   ([1,5,5] and [11])

    Input:  nums = [1,2,3,5]
    Output: False

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100
"""

def can_partition(nums: list[int]) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False
    assert can_partition([1, 1]) == True
    assert can_partition([2, 2, 3, 5]) == False
    assert can_partition([3, 3, 3, 4, 5]) == True
    print("All tests passed!")
