"""
Employee Free Time
-------------------
We are given a list schedule of employees, which represents the working time
for each employee. Each employee has a list of non-overlapping Intervals, and
these intervals are sorted. Return the list of finite intervals representing
the common, positive-length free time for all employees, also in sorted order.

Note: Even though we're representing Intervals in the input as [[s1, e1], ...],
the result should also be a list of intervals.

Example:
    Input:  schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
    Output: [[5,6],[7,9]]

    Input:  schedule = [[[1,3],[6,7]], [[2,4]]]
    Output: [[4,6]]

Constraints:
    - 1 <= schedule.length, schedule[i].length <= 50
    - 0 <= schedule[i][j].start < schedule[i][j].end <= 10^8
"""

def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert employee_free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]) == [[5, 6], [7, 9]]
    assert employee_free_time([[[1, 3], [6, 7]], [[2, 4]]]) == [[4, 6]]
    assert employee_free_time([[[1, 2], [5, 6]], [[3, 4]]]) == [[2, 3], [4, 5]]
    print("All tests passed!")
