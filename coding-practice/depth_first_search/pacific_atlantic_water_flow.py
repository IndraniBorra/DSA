"""
Pacific Atlantic Water Flow
-----------------------------
There is an m x n rectangular island. Rain water can flow to neighboring cells
(north, south, east, west) if the neighbor's height is <= current height.

The Pacific ocean touches the island's left and top edges.
The Atlantic ocean touches the island's right and bottom edges.

Return a list of grid coordinates [ri, ci] where rain water can flow to
BOTH the Pacific and Atlantic ocean.

Example:
    Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Input:  heights = [[1]]
    Output: [[0,0]]

Constraints:
    - m == heights.length, n == heights[r].length
    - 1 <= m, n <= 200
    - 0 <= heights[r][c] <= 10^5
"""

def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def sorted_result(res):
        return sorted([tuple(r) for r in res])

    h1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    expected1 = [(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)]
    assert sorted_result(pacific_atlantic(h1)) == expected1

    assert sorted_result(pacific_atlantic([[1]])) == [(0, 0)]

    print("All tests passed!")
