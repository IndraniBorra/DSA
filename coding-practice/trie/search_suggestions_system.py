"""
Search Suggestions System
--------------------------
You are given an array of strings products and a string searchWord. Design a
system that suggests at most three product names from products after each
character of searchWord is typed.

Suggested products should have a common prefix with searchWord.
If there are more than three products with a common prefix, return the three
lexicographically minimum products.

Return a list of lists of suggested products after each character of searchWord is typed.

Example:
    Input:  products = ["mobile","mouse","moneypot","monitor","mousepad"],
            searchWord = "mouse"
    Output: [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]

    Input:  products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Constraints:
    - 1 <= products.length <= 1000
    - 1 <= products[i].length <= 3000
    - 1 <= searchWord.length <= 1000
    - products[i] and searchWord consist of lowercase English letters
    - All strings in products are unique
"""

def suggested_products(products: list[str], search_word: str) -> list[list[str]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    r1 = suggested_products(
        ["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
    assert r1 == [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]

    r2 = suggested_products(["havana"], "havana")
    assert r2 == [["havana"]]*6

    print("All tests passed!")
