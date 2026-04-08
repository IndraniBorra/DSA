"""
Linked List Cycle
------------------
Given head, the head of a linked list, determine if the linked list has a cycle.
A cycle exists if some node can be reached again by continuously following the next pointer.

Return True if there is a cycle, False otherwise.

Example:
    Input:  3 -> 2 -> 0 -> -4 -> (back to node with value 2)
    Output: True

    Input:  1 -> 2 -> (back to node 1)
    Output: True

    Input:  1
    Output: False

Constraints:
    - The number of nodes in the list is in the range [0, 10^4]
    - -10^5 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Test 1: cycle exists  3 -> 2 -> 0 -> -4 -> (back to node 2)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node4 = ListNode(-4)
    node3.next = node2; node2.next = node0; node0.next = node4; node4.next = node2
    assert has_cycle(node3) == True

    # Test 2: no cycle
    a = ListNode(1); b = ListNode(2)
    a.next = b
    assert has_cycle(a) == False

    # Test 3: single node
    assert has_cycle(ListNode(1)) == False

    # Test 4: empty
    assert has_cycle(None) == False

    print("All tests passed!")
