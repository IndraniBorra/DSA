"""
Walls and Gates (Fill Matrix with Distance to Nearest Gate)
-------------------------------------------------------------
You are given an m x n grid rooms initialized with these three possible values:
  -1  — A wall or obstacle
   0  — A gate
   INF (2^31 - 1) — An empty room

Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, that room should remain INF.

Example:
    Input:
        INF  -1   0   INF
        INF  INF  INF  -1
        INF  -1   INF  -1
         0   -1   INF  INF

    Output:
         3  -1   0   1
         2   2   1  -1
         1  -1   2  -1
         0  -1   3   4

Constraints:
    - m == rooms.length, n == rooms[i].length
    - 1 <= m, n <= 250
    - rooms[i][j] is -1, 0, or 2^31 - 1
"""

INF = 2**31 - 1


def walls_and_gates(rooms: list[list[int]]) -> None:
    """Modifies rooms in-place."""
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    grid = [[INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0,   -1, INF, INF]]
    walls_and_gates(grid)
    assert grid == [[3, -1, 0, 1],
                    [2,  2, 1, -1],
                    [1, -1, 2, -1],
                    [0, -1, 3, 4]]

    grid2 = [[-1]]
    walls_and_gates(grid2)
    assert grid2 == [[-1]]

    print("All tests passed!")
