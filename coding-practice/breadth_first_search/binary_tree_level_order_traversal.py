"""
Binary Tree Level Order Traversal
-----------------------------------
Given the root of a binary tree, return the level order traversal of its
nodes' values (i.e., from left to right, level by level).

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input:  root = [1]
    Output: [[1]]

    Input:  root = []
    Output: []

Constraints:
    - The number of nodes is in the range [0, 2000]
    - -1000 <= Node.val <= 1000
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root1) == [[3], [9, 20], [15, 7]]

    assert level_order(TreeNode(1)) == [[1]]

    assert level_order(None) == []

    print("All tests passed!")
