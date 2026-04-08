"""
Non-Overlapping Intervals
--------------------------
Given an array of intervals intervals where intervals[i] = [start_i, end_i],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.

Example:
    Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1   (remove [1,3])

    Input:  intervals = [[1,2],[1,2],[1,2]]
    Output: 2   (keep one [1,2], remove the other two)

    Input:  intervals = [[1,2],[2,3]]
    Output: 0   (already non-overlapping)

Constraints:
    - 1 <= intervals.length <= 10^5
    - intervals[i].length == 2
    - -5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    assert erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    print("All tests passed!")
