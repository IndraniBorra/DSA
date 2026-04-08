"""
Shortest Path in Binary Matrix
--------------------------------
Given an n x n binary matrix grid, return the length of the shortest clear path
from top-left (0,0) to bottom-right (n-1,n-1). A clear path only steps on cells
with value 0 and moves 8-directionally. The path length is the number of cells visited.

If no such path exists, return -1.

Example:
    Input:  grid = [[0,1],[1,0]]
    Output: 2

    Input:  grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

    Input:  grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1   (start cell is blocked)

Constraints:
    - n == grid.length == grid[i].length
    - 1 <= n <= 100
    - grid[i][j] is 0 or 1
"""

def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert shortest_path_binary_matrix([[0,1],[1,0]]) == 2
    assert shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]) == 4
    assert shortest_path_binary_matrix([[1,0,0],[1,1,0],[1,1,0]]) == -1
    assert shortest_path_binary_matrix([[0]]) == 1
    print("All tests passed!")
