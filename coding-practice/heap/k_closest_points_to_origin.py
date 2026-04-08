"""
K Closest Points to Origin
----------------------------
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance is the Euclidean distance: sqrt(x^2 + y^2).
You may return the answer in any order.

Example:
    Input:  points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation: sqrt(8) < sqrt(10), so [-2,2] is closer.

    Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]

Constraints:
    - 1 <= k <= points.length <= 10^4
    - -10^4 <= xi, yi <= 10^4
"""

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def sorted_pts(pts):
        return sorted([tuple(p) for p in pts])

    assert sorted_pts(k_closest([[1, 3], [-2, 2]], 1)) == [(-2, 2)]
    assert sorted_pts(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == sorted_pts([[3, 3], [-2, 4]])
    assert sorted_pts(k_closest([[0, 1], [1, 0]], 2)) == [(0, 1), (1, 0)]
    print("All tests passed!")
