"""
Can Attend Meetings
--------------------
Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
determine if a person could attend all meetings (no two meetings overlap).

Example:
    Input:  intervals = [[0,30],[5,10],[15,20]]
    Output: False   (meeting [0,30] overlaps with [5,10])

    Input:  intervals = [[7,10],[2,4]]
    Output: True

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i < end_i <= 10^6
"""

def can_attend_meetings(intervals: list[list[int]]) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) == False
    assert can_attend_meetings([[7, 10], [2, 4]]) == True
    assert can_attend_meetings([]) == True
    assert can_attend_meetings([[1, 5], [5, 10]]) == True   # touching but not overlapping
    assert can_attend_meetings([[1, 10], [2, 3]]) == False
    print("All tests passed!")
