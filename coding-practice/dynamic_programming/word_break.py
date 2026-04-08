"""
Word Break
-----------
Given a string s and a dictionary of strings wordDict, return True if s can
be segmented into a space-separated sequence of one or more dictionary words.

Note: The same word in the dictionary may be reused multiple times in the segmentation.

Example:
    Input:  s = "leetcode", wordDict = ["leet","code"]
    Output: True

    Input:  s = "applepenapple", wordDict = ["apple","pen"]
    Output: True

    Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: False

Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters
    - All strings in wordDict are unique
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) == True
    assert word_break("applepenapple", ["apple", "pen"]) == True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert word_break("a", ["a"]) == True
    assert word_break("ab", ["a", "b"]) == True
    print("All tests passed!")
