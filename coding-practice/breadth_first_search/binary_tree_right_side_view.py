"""
Binary Tree Right Side View
-----------------------------
Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.

Example:
    Input:  root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

    Input:  root = [1,null,3]
    Output: [1,3]

    Input:  root = []
    Output: []

Constraints:
    - The number of nodes is in the range [0, 100]
    - -100 <= Node.val <= 100
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(1,
                TreeNode(2, None, TreeNode(5)),
                TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root1) == [1, 3, 4]

    root2 = TreeNode(1, None, TreeNode(3))
    assert right_side_view(root2) == [1, 3]

    assert right_side_view(None) == []

    print("All tests passed!")
