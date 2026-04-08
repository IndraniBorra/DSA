"""
Insert Interval
----------------
You are given an array of non-overlapping intervals sorted by start time,
and a new interval. Insert the new interval into the correct position and
merge if necessary.

Return the resulting array of non-overlapping intervals after the insertion.

Example:
    Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^5
    - intervals is sorted by start_i in ascending order
    - newInterval.length == 2
"""

def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert insert([], [5, 7]) == [[5, 7]]
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    print("All tests passed!")
