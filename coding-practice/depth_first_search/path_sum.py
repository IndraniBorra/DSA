"""
Path Sum
---------
Given the root of a binary tree and an integer targetSum, return True if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum.

A leaf is a node with no children.

Example:
    Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: True   (path: 5 → 4 → 11 → 2)

    Input:  root = [1,2,3], targetSum = 5
    Output: False

    Input:  root = [], targetSum = 0
    Output: False

Constraints:
    - The number of nodes is in the range [0, 5000]
    - -1000 <= Node.val <= 1000
    - -1000 <= targetSum <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert has_path_sum(root1, 22) == True

    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert has_path_sum(root2, 5) == False

    assert has_path_sum(None, 0) == False

    assert has_path_sum(TreeNode(1, TreeNode(2)), 1) == False
    assert has_path_sum(TreeNode(1, TreeNode(2)), 3) == True

    print("All tests passed!")
