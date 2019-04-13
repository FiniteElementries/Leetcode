# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    max_depth = 0
    def dfs(self, node, depth):
        if depth > self.max_depth:
            self.max_depth = depth
        if node is None:
            return
        else:
            self.dfs(node.left, depth + 1)
            self.dfs(node.right, depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root, 0)

        return self.max_depth

