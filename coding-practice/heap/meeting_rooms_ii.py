"""
Meeting Rooms II
-----------------
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required.

Example:
    Input:  intervals = [[0,30],[5,10],[15,20]]
    Output: 2

    Input:  intervals = [[7,10],[2,4]]
    Output: 1

Constraints:
    - 1 <= intervals.length <= 10^4
    - 0 <= start_i < end_i <= 10^6
"""

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7]]) == 3
    assert min_meeting_rooms([[1, 4], [4, 5]]) == 1
    assert min_meeting_rooms([[1, 10], [2, 3], [4, 5], [6, 7]]) == 2
    print("All tests passed!")
