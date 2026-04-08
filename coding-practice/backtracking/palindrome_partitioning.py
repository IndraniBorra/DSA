"""
Palindrome Partitioning
------------------------
Given a string s, partition s such that every substring of the partition is
a palindrome. Return all possible palindrome partitioning of s.

Example:
    Input:  s = "aab"
    Output: [["a","a","b"],["aa","b"]]

    Input:  s = "a"
    Output: [["a"]]

Constraints:
    - 1 <= s.length <= 16
    - s consists of only lowercase English letters
"""

def partition(s: str) -> list[list[str]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def normalize(result):
        return sorted([tuple(p) for p in result])

    assert normalize(partition("aab")) == normalize([["a","a","b"],["aa","b"]])
    assert normalize(partition("a")) == [("a",)]
    assert normalize(partition("aa")) == normalize([["a","a"],["aa"]])
    assert normalize(partition("aba")) == normalize([["a","b","a"],["aba"]])
    print("All tests passed!")
