# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    total = 0
    L = 0
    R = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        self.total = 0
        self.L = L
        self.R = R

        self.findNode(root)

        return self.total

    def findNode(self, node: TreeNode):
        if node is None:
            return None

        if node.val < self.L:
            self.findNode(node.right)

        elif node.val > self.R:
            self.findNode(node.left)

        else:
            self.total += node.val
            self.findNode(node.left)
            self.findNode(node.right)


