"""
Longest Substring Without Repeating Characters
------------------------------------------------
Given a string s, find the length of the longest substring without
repeating characters.

Example:
    Input:  s = "abcabcbb"
    Output: 3   ("abc")

    Input:  s = "bbbbb"
    Output: 1   ("b")

    Input:  s = "pwwkew"
    Output: 3   ("wke")

Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces
"""

def length_of_longest_substring(s: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("dvdf") == 3
    print("All tests passed!")
