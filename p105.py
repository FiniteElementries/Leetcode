from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def insert(self, val, index, node):
        if index < self.index_map[node.val]:
            if node.left is not None:
                self.insert(val, index, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if node.right is not None:
                self.insert(val, index, node.right)
            else:
                node.right = TreeNode(val)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        count = len(preorder)

        self.index_map = {}

        root = None
        for i in range(count):
            for j in range(count):
                if preorder[i] == inorder[j]:
                    self.index_map[inorder[j]] = j
                    if not root:
                        root = TreeNode(inorder[j])
                    else:
                        self.insert(inorder[j], j, root)
                    break
        return root
