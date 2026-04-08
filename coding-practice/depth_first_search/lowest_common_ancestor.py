"""
Lowest Common Ancestor of a Binary Tree
-----------------------------------------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes.

The LCA is defined as the lowest node that has both p and q as descendants
(where a node can be a descendant of itself).

Example:
    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3

    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5   (5 is an ancestor of 4)

Constraints:
    - The number of nodes is in the range [2, 10^5]
    - All Node.val are unique
    - p != q
    - p and q will exist in the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6); n2 = TreeNode(2); n0 = TreeNode(0); n8 = TreeNode(8)
    n7 = TreeNode(7); n4 = TreeNode(4)

    n3.left = n5; n3.right = n1
    n5.left = n6; n5.right = n2
    n1.left = n0; n1.right = n8
    n2.left = n7; n2.right = n4

    assert lowest_common_ancestor(n3, n5, n1).val == 3
    assert lowest_common_ancestor(n3, n5, n4).val == 5
    assert lowest_common_ancestor(n3, n6, n4).val == 5

    print("All tests passed!")
