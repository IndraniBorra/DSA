"""
Word Ladder
------------
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence beginWord → s1 → s2 → ... → endWord such that:
  - Every adjacent pair differs by exactly one letter
  - Every si is in wordList

Return the number of words in the shortest transformation sequence, or 0 if
no such sequence exists.

Example:
    Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5   (hit → hot → dot → dog → cog)

    Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: 0   ("cog" not in wordList)

Constraints:
    - 1 <= beginWord.length <= 10
    - endWord.length == beginWord.length
    - 1 <= wordList.length <= 5000
    - wordList[i].length == beginWord.length
    - All words consist of lowercase English letters
    - beginWord != endWord
    - All words in wordList are unique
"""

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert ladder_length("a", "c", ["a","b","c"]) == 2
    print("All tests passed!")
