# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def update_left(self, stack):
        node = stack.pop()
        node = node.right
        while node is not None:
            stack.append(node)
            node = node.left

    def update_right(self, stack):
        node = stack.pop()
        node = node.left
        while node is not None:
            stack.append(node)
            node = node.right

    def findTarget(self, root: TreeNode, k: int) -> bool:

        node = root
        left_stack = []
        while node is not None:
            left_stack.append(node)
            node = node.left

        node = root
        right_stack = []
        while node is not None:
            right_stack.append(node)
            node = node.right

        while len(left_stack) > 0 and len(right_stack) > 0 and left_stack[-1] != right_stack[-1]:
            if left_stack[-1].val + right_stack[-1].val > k:
                self.update_right(right_stack)
            elif left_stack[-1].val + right_stack[-1].val < k:
                self.update_left(left_stack)
            else:
                return True
        return False


if __name__ == '__main__':

    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(s.findTarget(root, 3))