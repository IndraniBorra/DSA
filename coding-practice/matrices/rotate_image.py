"""
Rotate Image
-------------
You are given an n x n 2D matrix representing an image. Rotate the image
by 90 degrees (clockwise) in-place.

You must rotate the image in-place, which means you have to modify the input
2D matrix directly. Do NOT allocate another 2D matrix to do the rotation.

Example:
    Input:  [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Hint: Transpose then reverse each row.

Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000
"""

def rotate(matrix: list[list[int]]) -> None:
    """Modifies matrix in-place."""
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(m1)
    assert m1 == [[7,4,1],[8,5,2],[9,6,3]]

    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(m2)
    assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    m3 = [[1]]
    rotate(m3)
    assert m3 == [[1]]

    print("All tests passed!")
