from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []

        while len(stack):
            top = stack.pop()
            if top:
                res.append(top.val)
                stack.append(top.right)
                stack.append(top.left)

        return res

