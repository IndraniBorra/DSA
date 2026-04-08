"""
Sliding Window Maximum
-----------------------
You are given an array of integers nums and an integer k. There is a sliding
window of size k moving from left to right. At each position, you can only see
the k numbers in the window. Return the maximum value in each window.

Example:
    Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Window:  [1 3 -1] -3  5  3  6  7  → max 3
              1 [3 -1 -3] 5  3  6  7  → max 3
              1  3 [-1 -3  5] 3  6  7  → max 5
              1  3  -1 [-3  5  3] 6  7  → max 5
              1  3  -1  -3 [5  3  6] 7  → max 6
              1  3  -1  -3  5 [3  6  7] → max 7

    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length
"""

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([1,-1], 1) == [1,-1]
    assert max_sliding_window([9,11], 2) == [11]
    assert max_sliding_window([4,-2], 2) == [4]
    print("All tests passed!")
