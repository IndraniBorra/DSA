"""
Minimum Depth of Binary Tree
------------------------------
Given a binary tree, find its minimum depth. The minimum depth is the number
of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 2

    Input:  root = [2,null,3,null,4,null,5,null,6]
    Output: 5

Constraints:
    - The number of nodes is in the range [0, 10^5]
    - -1000 <= Node.val <= 1000
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: TreeNode) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert min_depth(root1) == 2

    # Right-skewed tree: 2 -> 3 -> 4 -> 5 -> 6
    root2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert min_depth(root2) == 5

    assert min_depth(None) == 0

    assert min_depth(TreeNode(1)) == 1

    print("All tests passed!")
