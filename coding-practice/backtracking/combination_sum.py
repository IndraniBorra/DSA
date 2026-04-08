"""
Combination Sum
----------------
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations where the chosen numbers sum to target.
The same number may be chosen from candidates an unlimited number of times.

The combinations may be returned in any order.

Example:
    Input:  candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

    Input:  candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

    Input:  candidates = [2], target = 1
    Output: []

Constraints:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - All candidates are distinct
    - 1 <= target <= 40
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def normalize(result):
        return sorted([sorted(c) for c in result])

    assert normalize(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert normalize(combination_sum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert normalize(combination_sum([2], 1)) == []
    print("All tests passed!")
