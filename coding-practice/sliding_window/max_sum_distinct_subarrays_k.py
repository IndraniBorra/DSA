"""
Maximum Sum of Distinct Subarrays With Length K
-------------------------------------------------
Given an integer array nums and an integer k, find the maximum subarray sum
of all subarrays of nums that meet the following conditions:
  - The length of the subarray is k, AND
  - All elements of the subarray are distinct.

Return the maximum subarray sum of all subarrays that meet the conditions.
If no subarray meets the conditions, return 0.

Example:
    Input:  nums = [1,5,4,2,9,9,9], k = 3
    Output: 15   (subarray [1,5,4] or [4,2,9])

    Input:  nums = [4,4,4], k = 3
    Output: 0    (no valid subarray with all distinct elements)

Constraints:
    - 1 <= k <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^5
"""

def maximum_subarray_sum(nums: list[int], k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert maximum_subarray_sum([1, 5, 4, 2, 9, 9, 9], 3) == 15
    assert maximum_subarray_sum([4, 4, 4], 3) == 0
    assert maximum_subarray_sum([1, 2, 3, 4], 2) == 7
    assert maximum_subarray_sum([1, 1, 1, 7, 8, 9], 3) == 24
    print("All tests passed!")
