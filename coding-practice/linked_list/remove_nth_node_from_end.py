"""
Remove Nth Node From End of List
----------------------------------
Given the head of a linked list, remove the n-th node from the end of the
list and return its head.

Could you do it in one pass?

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

    Input:  1, n = 1
    Output: (empty)

    Input:  1 -> 2, n = 1
    Output: 1

Constraints:
    - The number of nodes in the list is sz
    - 1 <= sz <= 30
    - 0 <= Node.val <= 100
    - 1 <= n <= sz
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    pass


# ── Helper ─────────────────────────────────────────────────────────────────────
def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next

def list_to_array(head):
    result = []
    while head:
        result.append(head.val); head = head.next
    return result


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert list_to_array(remove_nth_from_end(make_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert list_to_array(remove_nth_from_end(make_list([1]), 1)) == []
    assert list_to_array(remove_nth_from_end(make_list([1, 2]), 1)) == [1]
    assert list_to_array(remove_nth_from_end(make_list([1, 2]), 2)) == [2]
    print("All tests passed!")
