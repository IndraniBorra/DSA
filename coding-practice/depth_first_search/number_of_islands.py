"""
Number of Islands
------------------
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. Assume all four edges of the grid are all surrounded by water.

Example:
    Input:
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
    Output: 1

    Input:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    Output: 3

Constraints:
    - m == grid.length, n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'
"""

def num_islands(grid: list[list[str]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    g1 = [["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
    assert num_islands(g1) == 1

    g2 = [["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]]
    assert num_islands(g2) == 3

    g3 = [["1"]]
    assert num_islands(g3) == 1

    g4 = [["0"]]
    assert num_islands(g4) == 0

    print("All tests passed!")
