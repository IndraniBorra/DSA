"""
Binary Tree Zigzag Level Order Traversal
------------------------------------------
Given the root of a binary tree, return the zigzag level order traversal of
its nodes' values (i.e., from left to right, then right to left for the next
level and alternate between).

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

    Input:  root = [1]
    Output: [[1]]

    Input:  root = []
    Output: []

Constraints:
    - The number of nodes is in the range [0, 2000]
    - -100 <= Node.val <= 100
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag_level_order(root1) == [[3], [20, 9], [15, 7]]

    assert zigzag_level_order(TreeNode(1)) == [[1]]

    assert zigzag_level_order(None) == []

    print("All tests passed!")
