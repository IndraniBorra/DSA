"""
Next Largest Number to the Right
--------------------------------
Given an integer array nums, return an output array res where, for each value
nums[i], res[i] is the first number to the right that's larger than nums[i].
If no larger number exists to the right of nums[i], set res[i] to -1.

Example:
    Input:  nums = [5, 2, 4, 6, 1]
    Output: [6, 4, 6, -1, -1]

Idea (monotonic decreasing stack):
    Scan the array from RIGHT to LEFT, keeping a stack of "candidates" — the
    values seen so far that could still be someone's next-larger number. Before
    answering for the current value, pop every candidate that is <= it (they can
    never win against the current value for anything further left). Whatever is
    left on top of the stack is the answer; then push the current value.

    The stack always stays in strictly decreasing order (top = smallest).

Complexity:
    Time:  O(n) — each value is pushed and popped at most once.
    Space: O(n) — the stack can hold all n values in the worst case.
"""
from typing import List


def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    stack = []  # candidates, kept in strictly decreasing order (top = smallest)

    # Walk from the rightmost element to the left.
    for i in range(len(nums) - 1, -1, -1):
        # Pop candidates that can't beat the current value.
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        # Top of stack (if any) is the next larger number to the right.
        res[i] = stack[-1] if stack else -1
        # Current value becomes a candidate for values further left.
        stack.append(nums[i])

    return res


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert next_largest_number_to_the_right([5, 2, 4, 6, 1]) == [6, 4, 6, -1, -1]
    assert next_largest_number_to_the_right([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert next_largest_number_to_the_right([4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert next_largest_number_to_the_right([2, 2, 2]) == [-1, -1, -1]
    assert next_largest_number_to_the_right([5]) == [-1]
    assert next_largest_number_to_the_right([]) == []
    print("All tests passed!")
