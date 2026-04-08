"""
Same Tree
----------
Given the roots of two binary trees p and q, write a function to check if
they are the same or not. Two binary trees are considered the same if they
are structurally identical, and the nodes have the same value.

Example:
    Input:  p = [1,2,3], q = [1,2,3]
    Output: True

    Input:  p = [1,2], q = [1,null,2]
    Output: False

    Input:  p = [1,2,1], q = [1,1,2]
    Output: False

Constraints:
    - The number of nodes in both trees is in the range [0, 100]
    - -10^4 <= Node.val <= 10^4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def make(v, l=None, r=None): return TreeNode(v, l, r)

    assert is_same_tree(make(1, make(2), make(3)), make(1, make(2), make(3))) == True
    assert is_same_tree(make(1, make(2)), make(1, None, make(2))) == False
    assert is_same_tree(make(1, make(2), make(1)), make(1, make(1), make(2))) == False
    assert is_same_tree(None, None) == True
    assert is_same_tree(make(1), None) == False

    print("All tests passed!")
