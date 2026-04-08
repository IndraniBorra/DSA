"""
Maximum Sum of Subarrays of Size K
-------------------------------------
Given an array of integers and a number k, find the maximum sum of any
contiguous subarray of size k.

Example:
    Input:  nums = [2,1,5,1,3,2], k = 3
    Output: 9   (subarray [5,1,3])

    Input:  nums = [2,3,4,1,5], k = 2
    Output: 7   (subarray [3,4])

Constraints:
    - 1 <= k <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
"""

def max_sum_subarray(nums: list[int], k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray([2, 3, 4, 1, 5], 2) == 7
    assert max_sum_subarray([1, 2, 3, 4, 5], 1) == 5
    assert max_sum_subarray([-1, -2, -3, -4], 2) == -3
    print("All tests passed!")
