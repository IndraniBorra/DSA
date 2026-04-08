"""
N-Queens
---------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other (no two queens share the same row,
column, or diagonal).

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' indicates a queen and '.' indicates an empty space.

Example:
    Input:  n = 4
    Output: [
        [".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]
    ]

    Input:  n = 1
    Output: [["Q"]]

Constraints:
    - 1 <= n <= 9
"""

def solve_n_queens(n: int) -> list[list[str]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def normalize(result):
        return sorted([tuple(r) for r in result])

    r4 = solve_n_queens(4)
    assert len(r4) == 2
    assert normalize(r4) == normalize([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])

    r1 = solve_n_queens(1)
    assert r1 == [["Q"]]

    assert len(solve_n_queens(8)) == 92   # classic result
    print("All tests passed!")
