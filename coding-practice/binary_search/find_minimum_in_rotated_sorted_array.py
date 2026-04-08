"""
Find Minimum in Rotated Sorted Array
--------------------------------------
Suppose an array of length n sorted in ascending order is rotated between
1 and n times. Given the rotated array nums of unique elements, return the
minimum element.

You must write an algorithm that runs in O(log n) time.

Example:
    Input:  nums = [3,4,5,1,2]
    Output: 1

    Input:  nums = [4,5,6,7,0,1,2]
    Output: 0

    Input:  nums = [11,13,15,17]
    Output: 11  (not rotated)

Constraints:
    - n == nums.length
    - 1 <= n <= 5000
    - -5000 <= nums[i] <= 5000
    - All integers are unique
    - nums is sorted and rotated between 1 and n times
"""

def find_min(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    print("All tests passed!")
