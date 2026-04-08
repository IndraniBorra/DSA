"""
Longest Valid Parentheses
--------------------------
Given a string containing just the characters '(' and ')', return the length
of the longest valid (well-formed) parentheses substring.

Example:
    Input:  s = "(()"
    Output: 2   (longest valid is "()")

    Input:  s = ")()())"
    Output: 4   (longest valid is "()()")

    Input:  s = ""
    Output: 0

Constraints:
    - 0 <= s.length <= 3 * 10^4
    - s[i] is '(' or ')'
"""

def longest_valid_parentheses(s: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0
    assert longest_valid_parentheses("()") == 2
    assert longest_valid_parentheses("()(()") == 2
    assert longest_valid_parentheses("((()))") == 6
    print("All tests passed!")
