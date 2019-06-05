from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    preorder_ind = 0
    ind_map = {}
    def buildNode(self, preorder, inorder, inorder_start, inorder_end):

        if self.preorder_ind >= len(preorder):
            return None

        if inorder_start > inorder_end:
            return None

        new_node = TreeNode(preorder[self.preorder_ind])
        self.preorder_ind += 1

        i = self.ind_map[new_node.val]

        new_node.left = self.buildNode(preorder, inorder, inorder_start, i-1)
        new_node.right = self.buildNode(preorder, inorder, i + 1, inorder_end)
        return new_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder_ind = 0
        self.ind_map = {}
        for i in range(len(inorder)):
            self.ind_map[inorder[i]] = i

        return self.buildNode(preorder, inorder, 0, len(preorder) - 1)

if __name__ == "__main__":
    s = Solution()

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    print(s.buildTree(preorder, inorder))