"""
Partition Labels
-----------------
You are given a string s. We want to partition the string into as many parts
as possible so that each letter appears in at most one part.

Return a list of integers representing the size of each part.

Example:
    Input:  s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
        "ababcbaca" — all a, b, c are only in this part
        "defegde"  — all d, e, f, g are only in this part
        "hijhklij" — all h, i, j, k, l are only in this part

    Input:  s = "eccbbbbdec"
    Output: [10]

Constraints:
    - 1 <= s.length <= 500
    - s consists of lowercase English letters only
"""

def partition_labels(s: str) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_labels("eccbbbbdec") == [10]
    assert partition_labels("a") == [1]
    assert partition_labels("abcd") == [1, 1, 1, 1]
    assert partition_labels("caedbdedda") == [1, 9]
    print("All tests passed!")
