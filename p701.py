"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        root = self.insert(root, val)
        return root

    def insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        elif val > node.val:
            node.right = self.insert(node.right, val)

        return node

