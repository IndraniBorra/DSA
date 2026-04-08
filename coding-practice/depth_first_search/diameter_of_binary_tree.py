"""
Diameter of Binary Tree
------------------------
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter is the length of the longest path between any two nodes. This path
may or may not pass through the root.

The length of a path is the number of edges between nodes.

Example:
    Input:
        1
       / \
      2   3
     / \
    4   5

    Output: 3   (path: 4 → 2 → 1 → 3  or  5 → 2 → 1 → 3)

    Input:  root = [1,2]
    Output: 1

Constraints:
    - The number of nodes is in the range [1, 10^4]
    - -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3))
    assert diameter_of_binary_tree(root1) == 3

    root2 = TreeNode(1, TreeNode(2))
    assert diameter_of_binary_tree(root2) == 1

    assert diameter_of_binary_tree(TreeNode(1)) == 0

    print("All tests passed!")
