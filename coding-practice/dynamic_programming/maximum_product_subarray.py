"""
Maximum Product Subarray
-------------------------
Given an integer array nums, find a subarray that has the largest product,
and return the product.

Note: The array may contain negative numbers and zeros.

Example:
    Input:  nums = [2,3,-2,4]
    Output: 6   (subarray [2,3])

    Input:  nums = [-2,0,-1]
    Output: 0   (subarray [0])

Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -10 <= nums[i] <= 10
    - The product of any subarray fits in a 32-bit integer
"""

def max_product(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2]) == -2
    assert max_product([0, 2]) == 2
    assert max_product([-2, 3, -4]) == 24
    assert max_product([2, -5, -2, -4, 3]) == 24
    print("All tests passed!")
