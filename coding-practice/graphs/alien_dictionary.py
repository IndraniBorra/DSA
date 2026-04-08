"""
Alien Dictionary
-----------------
There is a new alien language that uses the English alphabet. However, the order
of the letters is unknown. You are given a list of strings words from the alien
language's dictionary, where the strings are sorted lexicographically by the rules
of this new language.

Return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules. If there is no
solution, return "". If there are multiple solutions, return any.

Example:
    Input:  words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

    Input:  words = ["z","x"]
    Output: "zx"

    Input:  words = ["z","x","z"]
    Output: ""   (cycle detected)

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 100
    - words[i] consists of only lowercase English letters
"""

def alien_order(words: list[str]) -> str:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert alien_order(["wrt","wrf","er","ett","rftt"]) == "wertf"
    assert alien_order(["z","x"]) == "zx"
    assert alien_order(["z","x","z"]) == ""
    assert alien_order(["abc","ab"]) == ""   # invalid: longer word before prefix
    assert set(alien_order(["z"])) == {"z"}
    print("All tests passed!")
