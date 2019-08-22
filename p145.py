from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while len(stack):
            top = stack.pop()
            if top is not None:
                res.append(top)
                stack.append(top.left)
                stack.append(top.right)
        res.reverse()

        return [x.val for x in res]
