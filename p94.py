# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    inorder_traversal = []
    def dfs(self, node):
        if node is None:
            return
        else:
            self.dfs(node.left)
            self.inorder_traversal.append(node.val)
            self.dfs(node.right)

    def inorderTraversal(self, root: TreeNode):
        self.inorder_traversal = []
        self.dfs(root)
        return self.inorder_traversal

if __name__ == "__main__":

    root = TreeNode(1)
    root.right=TreeNode(2)
    root.right.left=TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root))