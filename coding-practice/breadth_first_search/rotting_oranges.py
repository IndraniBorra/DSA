"""
Rotting Oranges
----------------
You are given an m x n grid where each cell can have one of three values:
  0 — empty cell
  1 — fresh orange
  2 — rotten orange

Every minute, any fresh orange adjacent (4-directionally) to a rotten orange
becomes rotten. Return the minimum number of minutes until no fresh orange
remains, or -1 if it is impossible.

Example:
    Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1   (bottom-left orange is isolated)

    Input:  grid = [[0,2]]
    Output: 0    (no fresh oranges)

Constraints:
    - m == grid.length, n == grid[i].length
    - 1 <= m, n <= 10
    - grid[i][j] is 0, 1, or 2
"""

def oranges_rotting(grid: list[list[int]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert oranges_rotting([[0,2]]) == 0
    assert oranges_rotting([[2,2],[1,1],[0,0],[2,0]]) == 1
    print("All tests passed!")
