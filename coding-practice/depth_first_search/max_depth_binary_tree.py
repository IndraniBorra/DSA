"""
Maximum Depth of Binary Tree
------------------------------
Given the root of a binary tree, return its maximum depth.
Maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3

    Input:  root = [1,null,2]
    Output: 2

Constraints:
    - The number of nodes is in the range [0, 10^4]
    - -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #      / \
    #     15   7
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root1) == 3

    root2 = TreeNode(1, None, TreeNode(2))
    assert max_depth(root2) == 2

    assert max_depth(None) == 0

    assert max_depth(TreeNode(1)) == 1

    print("All tests passed!")
