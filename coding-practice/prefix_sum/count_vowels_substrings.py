"""
Count Vowels in Substrings
---------------------------
Given a 0-indexed string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', 'u')
in every substring of word.

A substring is a contiguous (non-empty) sequence of characters within a string.

Note: Due to the large number of substrings, compute this efficiently using prefix sums.

Example:
    Input:  word = "aba"
    Output: 6
    Substrings: a(1), ab(1), aba(2), b(0), ba(1), a(1) → total = 6

    Input:  word = "abc"
    Output: 3
    Substrings: a(1), ab(1), abc(1), b(0), bc(0), c(0) → total = 3

Constraints:
    - 1 <= word.length <= 10^5
    - word consists of lowercase English letters only
"""

def count_vowels(word: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert count_vowels("aba") == 6
    assert count_vowels("abc") == 3
    assert count_vowels("a") == 1
    assert count_vowels("bcd") == 0
    assert count_vowels("aeiou") == 35   # each vowel contributes i*(n-i) * ...
    print("All tests passed!")
