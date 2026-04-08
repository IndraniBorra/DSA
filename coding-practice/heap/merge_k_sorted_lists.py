"""
Merge K Sorted Lists
---------------------
You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order. Merge all the linked-lists into one sorted linked-list
and return it.

Example:
    Input:  lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Input:  lists = []
    Output: []

    Input:  lists = [[]]
    Output: []

Constraints:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
    - lists[i] is sorted in ascending order
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode]) -> ListNode:
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
    lists1 = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    assert list_to_array(merge_k_lists(lists1)) == [1, 1, 2, 3, 4, 4, 5, 6]

    assert list_to_array(merge_k_lists([])) == []
    assert list_to_array(merge_k_lists([make_list([])])) == []

    print("All tests passed!")
