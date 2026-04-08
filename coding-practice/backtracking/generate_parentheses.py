"""
Generate Parentheses
---------------------
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example:
    Input:  n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Input:  n = 1
    Output: ["()"]

Constraints:
    - 1 <= n <= 8
"""

def generate_parenthesis(n: int) -> list[str]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert sorted(generate_parenthesis(1)) == ["()"]
    assert sorted(generate_parenthesis(2)) == sorted(["(())", "()()"])
    assert sorted(generate_parenthesis(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])
    assert len(generate_parenthesis(4)) == 14    # Catalan number C(4)
    print("All tests passed!")
