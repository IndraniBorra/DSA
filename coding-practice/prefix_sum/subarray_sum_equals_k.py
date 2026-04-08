"""
Subarray Sum Equals K
----------------------
Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example:
    Input:  nums = [1,1,1], k = 2
    Output: 2

    Input:  nums = [1,2,3], k = 3
    Output: 2   ([1,2] and [3])

Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -1000 <= nums[i] <= 1000
    - -10^7 <= k <= 10^7
"""

def subarray_sum(nums: list[int], k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([1], 1) == 1
    assert subarray_sum([-1, -1, 1], 0) == 1
    assert subarray_sum([1, 2, 1, 2, 1], 3) == 4
    print("All tests passed!")
