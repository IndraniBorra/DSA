"""
Reorder List
-------------
You are given the head of a singly linked-list: L0 → L1 → … → Ln-1 → Ln

Reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example:
    Input:  1 -> 2 -> 3 -> 4
    Output: 1 -> 4 -> 2 -> 3

    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 5 -> 2 -> 4 -> 3

Constraints:
    - The number of nodes is in the range [1, 5 * 10^4]
    - 1 <= Node.val <= 1000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:
    """Modifies the list in-place."""
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
    h1 = make_list([1, 2, 3, 4])
    reorder_list(h1)
    assert list_to_array(h1) == [1, 4, 2, 3]

    h2 = make_list([1, 2, 3, 4, 5])
    reorder_list(h2)
    assert list_to_array(h2) == [1, 5, 2, 4, 3]

    h3 = make_list([1])
    reorder_list(h3)
    assert list_to_array(h3) == [1]

    print("All tests passed!")
