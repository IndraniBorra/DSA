"""
Spiral Matrix
--------------
Given an m x n matrix, return all elements of the matrix in spiral order
(clockwise from the top-left).

Example:
    Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Input:  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    - m == matrix.length, n == matrix[i].length
    - 1 <= m, n <= 10
    - -100 <= matrix[i][j] <= 100
"""

def spiral_order(matrix: list[list[int]]) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert spiral_order([[1]]) == [1]
    assert spiral_order([[1,2],[3,4]]) == [1,2,4,3]
    print("All tests passed!")
