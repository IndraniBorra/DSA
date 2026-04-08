"""
Course Schedule II
-------------------
There are a total of numCourses courses labeled from 0 to numCourses - 1.
You are given prerequisites where prerequisites[i] = [ai, bi] means take bi before ai.

Return a valid ordering of courses to finish all of them. If impossible (cycle), return [].

Example:
    Input:  numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]

    Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3] or [0,1,2,3]

    Input:  numCourses = 1, prerequisites = []
    Output: [0]

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
    - prerequisites[i].length == 2
    - All prerequisites pairs are distinct
"""

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def is_valid_order(order, num_courses, prereqs):
        if len(order) != num_courses:
            return False
        pos = {c: i for i, c in enumerate(order)}
        return all(pos[b] < pos[a] for a, b in prereqs)

    r1 = find_order(2, [[1, 0]])
    assert is_valid_order(r1, 2, [[1, 0]])

    r2 = find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    assert is_valid_order(r2, 4, [[1,0],[2,0],[3,1],[3,2]])

    assert find_order(2, [[1,0],[0,1]]) == []   # cycle

    r3 = find_order(1, [])
    assert r3 == [0]

    print("All tests passed!")
