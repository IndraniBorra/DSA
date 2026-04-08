"""
Longest Increasing Subsequence
--------------------------------
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example:
    Input:  nums = [10,9,2,5,3,7,101,18]
    Output: 4   ([2,3,7,101])

    Input:  nums = [0,1,0,3,2,3]
    Output: 4

    Input:  nums = [7,7,7,7,7,7,7]
    Output: 1

Can you do it in O(n log n)?

Constraints:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4
"""

def length_of_lis(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1
    assert length_of_lis([3, 1, 2]) == 2
    print("All tests passed!")
