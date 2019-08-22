# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def push_node(self, node):
        if node is None:
            return

        if node.left is not None:
            self.stack.append(node)
            self.push_node(node.left)

        elif node.right is not None:
            self.push_node(node.right)
            self.stack.append(node)

        else:
            self.stack.append(node)

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_node(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.left is not None:
            self.push_node(top.right)
        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':

    root = TreeNode(1)
    root.right = TreeNode(2)

    s = BSTIterator(root)

    while s.hasNext():
        print(s.next())
