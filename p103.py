from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        nodes = [root]
        levels = []

        direction = 'r'

        while len(nodes) > 0:
            level = []
            for item in nodes:
                level.append(item.val)
            if direction == 'r':
                levels.append(level)
                direction = 'l'
            else:
                levels.append(level[::-1])
                direction = 'r'
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes

        return levels