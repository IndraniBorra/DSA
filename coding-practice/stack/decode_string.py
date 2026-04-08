"""
Decode String
--------------
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is repeated exactly k times. k is a positive integer.

You may assume that the input string is always valid, with no extra white
spaces, square brackets are well-formed, etc. All letters in encoded_string
are lowercase.

Example:
    Input:  s = "3[a]2[bc]"
    Output: "aaabcbc"

    Input:  s = "3[a2[c]]"
    Output: "accaccacc"

    Input:  s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Constraints:
    - 1 <= s.length <= 30
    - s consists of lowercase English letters, digits, and square brackets '[]'
    - s is guaranteed to be a valid input
    - All integers in s are in range [1, 300]
"""

def decode_string(s: str) -> str:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"
    assert decode_string("2[2[a]]") == "aaaa"
    print("All tests passed!")
