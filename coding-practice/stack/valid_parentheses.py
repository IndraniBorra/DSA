"""
Valid Parentheses
------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
  1. Open brackets are closed by the same type of brackets.
  2. Open brackets are closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

Example:
    Input:  s = "()"
    Output: True

    Input:  s = "()[]{}"
    Output: True

    Input:  s = "(]"
    Output: False

    Input:  s = "([)]"
    Output: False

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'
"""
def is_valid(s: str) -> bool:

        stack = []
        mapping = {")":"(", "}":"{","]":"["}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0
        


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("]") == False
    assert is_valid("") == True
    print("All tests passed!")
