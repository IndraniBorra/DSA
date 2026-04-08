"""
Swap Nodes in Pairs
--------------------
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed).

Example:
    Input:  1 -> 2 -> 3 -> 4
    Output: 2 -> 1 -> 4 -> 3

    Input:  (empty)
    Output: (empty)

    Input:  1
    Output: 1

Constraints:
    - The number of nodes is in the range [0, 100]
    - 0 <= Node.val <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode) -> ListNode:
    pass


# ── Helper ─────────────────────────────────────────────────────────────────────
def make_list(vals):
    dummy = ListNode(0); cur = dummy
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
    assert list_to_array(swap_pairs(make_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert list_to_array(swap_pairs(make_list([]))) == []
    assert list_to_array(swap_pairs(make_list([1]))) == [1]
    assert list_to_array(swap_pairs(make_list([1, 2, 3]))) == [2, 1, 3]
    print("All tests passed!")
