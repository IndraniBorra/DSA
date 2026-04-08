"""
Subsets
--------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return in any order.

Example:
    Input:  nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Input:  nums = [0]
    Output: [[],[0]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - All the numbers in nums are unique
"""

def subsets(nums: list[int]) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def normalize(result):
        return sorted([sorted(s) for s in result])

    assert normalize(subsets([1, 2, 3])) == normalize([[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]])
    assert normalize(subsets([0])) == [[], [0]]
    assert len(subsets([1, 2, 3, 4])) == 16    # 2^4 subsets
    print("All tests passed!")
