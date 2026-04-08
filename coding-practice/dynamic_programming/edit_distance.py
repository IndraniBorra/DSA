"""
Edit Distance (Levenshtein Distance)
--------------------------------------
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

Allowed operations:
  - Insert a character
  - Delete a character
  - Replace a character

Example:
    Input:  word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: horse → rorse (replace h→r) → rose (delete r) → ros (delete e)

    Input:  word1 = "intention", word2 = "execution"
    Output: 5

Constraints:
    - 0 <= word1.length, word2.length <= 500
    - word1 and word2 consist of lowercase English letters
"""

def min_distance(word1: str, word2: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("a", "") == 1
    assert min_distance("", "a") == 1
    assert min_distance("abc", "abc") == 0
    print("All tests passed!")
