"""
Implement Trie (Prefix Tree)
------------------------------
Implement a trie with the following methods:
  - insert(word): Inserts the string word into the trie.
  - search(word): Returns True if word is in the trie (exact match).
  - starts_with(prefix): Returns True if any word in the trie starts with prefix.

Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")    → True
    trie.search("app")      → False
    trie.starts_with("app") → True
    trie.insert("app")
    trie.search("app")      → True

Constraints:
    - 1 <= word.length, prefix.length <= 2000
    - word and prefix consist only of lowercase English letters
    - At most 3 * 10^4 calls total to insert, search, and starts_with
"""

class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") == True
    assert t.search("app") == False
    assert t.starts_with("app") == True
    t.insert("app")
    assert t.search("app") == True

    t2 = Trie()
    t2.insert("hello")
    assert t2.search("hell") == False
    assert t2.starts_with("hel") == True
    assert t2.starts_with("world") == False

    print("All tests passed!")
