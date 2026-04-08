"""
Word Search
------------
Given an m x n grid of characters board and a string word, return True if word
exists in the grid. The word can be constructed from letters of sequentially
adjacent cells (horizontally or vertically). The same cell may not be used more than once.

Example:
    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: True

    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: True

    Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: False

Constraints:
    - m == board.length, n == board[i].length
    - 1 <= m, n <= 6
    - 1 <= word.length <= 15
    - board and word consist of only lowercase and uppercase English letters
"""

def exist(board: list[list[str]], word: str) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(b, "ABCCED") == True
    assert exist(b, "SEE") == True
    assert exist(b, "ABCB") == False
    assert exist([["a"]], "a") == True
    assert exist([["a","b"],["c","d"]], "abdc") == True
    print("All tests passed!")
