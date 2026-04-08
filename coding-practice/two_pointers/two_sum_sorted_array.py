"""
Two Sum (Sorted Array)
----------------------
Given a 1-indexed array of integers `numbers` that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Return the indices of the two numbers (1-indexed) as an
integer array [index1, index2] where 1 <= index1 < index2 <= numbers.length.

The solution must use only constant extra space.

Example:
    Input:  numbers = [2,7,11,15], target = 9
    Output: [1,2]

    Input:  numbers = [2,3,4], target = 6
    Output: [1,3]

    Input:  numbers = [-1,0], target = -1
    Output: [1,2]

Constraints:
    - 2 <= numbers.length <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - numbers is sorted in non-decreasing order
    - -1000 <= target <= 1000
    - Exactly one solution exists
"""

def two_sum(numbers: list[int], target: int) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    assert two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    print("All tests passed!")
