"""
Decode Ways
------------
A message containing letters A-Z can be encoded into numbers using:
    'A' → "1", 'B' → "2", ..., 'Z' → "26"

Given a string s containing only digits, return the number of ways to decode it.

Example:
    Input:  s = "12"
    Output: 2   ("AB" = 1+2, "L" = 12)

    Input:  s = "226"
    Output: 3   ("BZ"=2+26, "VF"=22+6, "BBF"=2+2+6)

    Input:  s = "06"
    Output: 0   (leading zero is invalid)

Constraints:
    - 1 <= s.length <= 100
    - s consists only of digits
    - s may contain leading zeros
"""

def num_decodings(s: str) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert num_decodings("0") == 0
    assert num_decodings("1") == 1
    assert num_decodings("11106") == 2
    assert num_decodings("10") == 1
    print("All tests passed!")
