"""
Palindrome Linked List
-----------------------
Given the head of a singly linked list, return True if it is a palindrome,
or False otherwise.

Could you do it in O(n) time and O(1) space?

Example:
    Input:  1 -> 2 -> 2 -> 1
    Output: True

    Input:  1 -> 2
    Output: False

Constraints:
    - The number of nodes is in the range [1, 10^5]
    - 0 <= Node.val <= 9
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    pass


# ── Helper ─────────────────────────────────────────────────────────────────────
def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert is_palindrome(make_list([1, 2, 2, 1])) == True
    assert is_palindrome(make_list([1, 2])) == False
    assert is_palindrome(make_list([1])) == True
    assert is_palindrome(make_list([1, 2, 3, 2, 1])) == True
    assert is_palindrome(make_list([1, 0, 0])) == False
    print("All tests passed!")
