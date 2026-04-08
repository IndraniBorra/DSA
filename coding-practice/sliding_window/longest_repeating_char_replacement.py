"""
Longest Repeating Character Replacement
-----------------------------------------
You are given a string s and an integer k. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation at most k times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.

Example:
    Input:  s = "ABAB", k = 2
    Output: 4   (Replace both A's or both B's → "AAAA" or "BBBB")

    Input:  s = "AABABBA", k = 1
    Output: 4

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only uppercase English letters
    - 0 <= k <= s.length
"""

def character_replacement(s: str, k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("ABCD", 2) == 3
    print("All tests passed!")
