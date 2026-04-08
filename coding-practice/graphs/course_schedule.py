"""
Course Schedule
----------------
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

Return True if you can finish all courses, False otherwise.
(Essentially: detect if the directed graph has a cycle.)

Example:
    Input:  numCourses = 2, prerequisites = [[1,0]]
    Output: True   (take 0, then 1)

    Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: False  (cycle: 0 → 1 → 0)

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
    - prerequisites[i].length == 2
    - 0 <= ai, bi < numCourses
    - All prerequisites pairs are unique
"""

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) == True
    assert can_finish(2, [[1, 0], [0, 1]]) == False
    assert can_finish(1, []) == True
    assert can_finish(5, [[1,0],[2,1],[3,2],[4,3]]) == True
    assert can_finish(4, [[1,0],[2,1],[3,2],[1,3]]) == False
    print("All tests passed!")
