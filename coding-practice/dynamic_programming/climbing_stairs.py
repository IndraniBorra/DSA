"""
Climbing Stairs
----------------
You are climbing a staircase. It takes n steps to reach the top. Each time
you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
    Input:  n = 2
    Output: 2   (1+1, 2)

    Input:  n = 3
    Output: 3   (1+1+1, 1+2, 2+1)

Constraints:
    - 1 <= n <= 45
"""

def climb_stairs(n: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    print("All tests passed!")
