"""
Unique Paths
-------------
There is a robot on an m x n grid. The robot is initially at the top-left
corner and is trying to reach the bottom-right corner. The robot can only
move either down or right at any point in time.

Given two integers m and n, return the number of unique paths.

Example:
    Input:  m = 3, n = 7
    Output: 28

    Input:  m = 3, n = 2
    Output: 3   (right→down→down, down→right→down, down→down→right)

Constraints:
    - 1 <= m, n <= 100
"""

def unique_paths(m: int, n: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(2, 2) == 2
    assert unique_paths(7, 3) == 28
    print("All tests passed!")
