"""
3-Sum
-----
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example:
    Input:  nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input:  nums = [0,1,1]
    Output: []

    Input:  nums = [0,0,0]
    Output: [[0,0,0]]

Constraints:
    - 3 <= nums.length <= 3000
    - -10^5 <= nums[i] <= 10^5
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def sorted_result(res):
        return sorted([sorted(t) for t in res])

    assert sorted_result(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert sorted_result(three_sum([0, 1, 1])) == []
    assert sorted_result(three_sum([0, 0, 0])) == [[0, 0, 0]]
    assert sorted_result(three_sum([-2, 0, 1, 1, 2])) == [[-2, 0, 2], [-2, 1, 1]]
    print("All tests passed!")
