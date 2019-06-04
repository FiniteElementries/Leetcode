# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        nodes = [root]

        while len(nodes) > 0:
            for i in range(0, len(nodes) // 2):
                j = len(nodes) - 1 - i
                if nodes[i] is None and nodes[j] is None:
                    continue
                if nodes[i] is None or nodes[j] is None:
                    return False

                if nodes[i].val == nodes[j].val:
                    continue
                return False

            new_nodes = []
            for node in nodes:
                if node:
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
            nodes = new_nodes
        return True


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(s.isSymmetric(root))
