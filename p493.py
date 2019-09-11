from typing import List


class Node(object):

    def __init__(self, val):
        self.count = 0
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def insert_node(self, node, val):
        if node is None:
            return Node(val)

        if val <= node.val * 2:
            node.left = self.insert_node(node.left, val)
        else:
            node.count += 1
            node.right = self.insert_node(node.right, val)
        return node

    def traverse_node(self, node):
        if not node:
            return 0

        count = node.count

        count += self.traverse_node(node.left)
        count += self.traverse_node(node.right)

        return count

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = Node(nums[-1])

        for i in range(len(nums) - 2, -1, -1):
            self.insert_node(root, nums[i])

        return self.traverse_node(root)