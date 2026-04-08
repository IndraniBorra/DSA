"""
Invert Binary Tree
-------------------
Given the root of a binary tree, invert the tree (mirror it), and return its root.

Example:
    Input:
         4
        / \
       2   7
      / \ / \
     1  3 6  9

    Output:
         4
        / \
       7   2
      / \ / \
     9  6 3  1

Constraints:
    - The number of nodes is in the range [0, 100]
    - -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    pass


# ── Helper ─────────────────────────────────────────────────────────────────────
def tree_to_list(root):
    """Level-order, None for missing nodes."""
    if not root:
        return []
    from collections import deque
    q, result = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left); q.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root1 = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))
    assert tree_to_list(invert_tree(root1)) == [4, 7, 2, 9, 6, 3, 1]

    assert invert_tree(None) is None

    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert tree_to_list(invert_tree(root2)) == [2, 3, 1]

    print("All tests passed!")
