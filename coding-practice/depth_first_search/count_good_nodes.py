"""
Count Good Nodes in Binary Tree
---------------------------------
Given a binary tree root, a node X in the tree is named good if in the path
from root to X there are no nodes with a value greater than X's value.

Return the number of good nodes in the binary tree.

Example:
    Input:  root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Good nodes: 3 (root), 4, 3 (left child of 1), 5

    Input:  root = [3,3,null,4,2]
    Output: 3

    Input:  root = [1]
    Output: 1

Constraints:
    - The number of nodes in the binary tree is in the range [1, 10^5]
    - Each node's value is between [-10, 10]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(3,
                TreeNode(1, TreeNode(3)),
                TreeNode(4, TreeNode(1), TreeNode(5)))
    assert good_nodes(root1) == 4

    root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    assert good_nodes(root2) == 3

    assert good_nodes(TreeNode(1)) == 1

    print("All tests passed!")
