# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    last_value = None
    valid = True
    def validate_node(self, node):
        if node is None:
            return

        if not self.valid:
            return

        self.validate_node(node.left)
        if self.last_value is None:
            self.last_value = node.val
        elif node.val < self.last_value:
            self.valid = False
        else:
            self.last_value = node.val

        self.validate_node(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.valid = True
        self.validate_node(root)
        return self.valid

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(1)

    # root = TreeNode(10)
    # root.left = TreeNode(5)
    # root.right = TreeNode(15)
    # root.right.left=TreeNode(6)
    # root.right.right = TreeNode(20)

    print(s.isValidBST(root))
