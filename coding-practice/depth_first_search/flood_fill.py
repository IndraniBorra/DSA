"""
Flood Fill
-----------
An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value.

You are given three integers sr, sc, and color. Perform a flood fill starting
from pixel image[sr][sc]: change that pixel and all pixels connected to it
(4-directionally) with the same color as image[sr][sc] to the new color.

Return the modified image.

Example:
    Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
    Output: [[2,2,2],[2,2,0],[2,0,1]]

    Input:  image = [[0,0,0],[0,0,0]], sr=0, sc=0, color=0
    Output: [[0,0,0],[0,0,0]]   (already same color)

Constraints:
    - m == image.length, n == image[i].length
    - 1 <= m, n <= 50
    - 0 <= image[i][j], color < 2^16
    - 0 <= sr < m, 0 <= sc < n
"""

def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert flood_fill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
    assert flood_fill([[1,2,2],[1,1,2],[1,1,1]], 1, 1, 3) == [[3,2,2],[3,3,2],[3,3,3]]
    print("All tests passed!")
