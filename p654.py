"""
https://leetcode.com/problems/maximum-binary-tree/submissions/

"""
# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            root = self.insertNode(root, nums[i])

        return root

    def insertNode(self, node: TreeNode, num: int):

        if node is None:
            node = TreeNode(num)
            return node

        if node.val >= num:
            node.right = self.insertNode(node.right, num)
            return node
        else:
            new_node = TreeNode(num)
            new_node.left = node
            return new_node


s = Solution()

s.constructMaximumBinaryTree([3,2,1,6,0,5])
