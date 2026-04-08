"""
Longest Common Subsequence
---------------------------
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence is a sequence derived from a string by deleting some or no
characters without changing the relative order of the remaining characters.

Example:
    Input:  text1 = "abcde", text2 = "ace"
    Output: 3   ("ace")

    Input:  text1 = "abc", text2 = "abc"
    Output: 3

    Input:  text1 = "abc", text2 = "def"
    Output: 0

Constraints:
    - 1 <= text1.length, text2.length <= 1000
    - text1 and text2 consist only of lowercase English letters
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bl", "yby") == 1
    assert longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    print("All tests passed!")
