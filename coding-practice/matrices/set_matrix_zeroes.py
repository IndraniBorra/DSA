"""
Set Matrix Zeroes
------------------
Given an m x n integer matrix, if an element is 0, set its entire row and
column to 0's. You must do it in-place.

Can you devise a constant space solution?

Example:
    Input:  [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    - m == matrix.length, n == matrix[0].length
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1
"""

def set_zeroes(matrix: list[list[int]]) -> None:
    """Modifies matrix in-place."""
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    set_zeroes(m1)
    assert m1 == [[1,0,1],[0,0,0],[1,0,1]]

    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_zeroes(m2)
    assert m2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    m3 = [[1,2,3]]
    set_zeroes(m3)
    assert m3 == [[1,2,3]]

    m4 = [[0]]
    set_zeroes(m4)
    assert m4 == [[0]]

    print("All tests passed!")
