from typing import List


class TreeNode(object):

    def __init__(self, val, rank):
        self.val = val
        self.left = None
        self.right = None
        self.rank = rank
        self.height = 1


class Solution:
    res = []

    def update_rank(self, node):
        if not node:
            return

        node.rank += 1

        self.update_rank(node.left)
        self.update_rank(node.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node

        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
        right.height = 1 + max(self.get_height(right.left), self.get_height(right.right))

        return right

    def rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node

        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
        left.height = 1 + max(self.get_height(left.left), self.get_height(left.right))

        return left

    def get_balance_value(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def insert_node(self, node, val, rank):
        if not node:
            self.res.append(rank)
            return TreeNode(val, rank)

        # insert node
        if val <= node.val:
            node.left = self.insert_node(node.left, val, node.rank)
            node.rank += 1
            self.update_rank(node.right)
        elif val > node.val:
            node.right = self.insert_node(node.right, val, node.rank + 1)

        # update node height
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))

        # balance tree
        balance_value = self.get_balance_value(node)

        if balance_value > 1 and val <= node.left.val:
            return self.rotate_right(node)

        if balance_value > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance_value < -1 and val > node.right.val:
            return self.rotate_left(node)

        if balance_value < -1 and val <= node.right.val:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        self.res = [0]
        root = TreeNode(nums[-1], 0)
        for i in range(len(nums) - 2, -1, -1):
            root = self.insert_node(root, nums[i], root.rank)

        self.res.reverse()
        return self.res


if __name__ == '__main__':
    s = Solution()

    nums = [5, 2, 6, 1]

    # nums = [0, 1, 2]
    #
    # # nums = [2, 0, 1]
    #
    # nums = [84, 66, 65, 36, 100, 41]
    #
    # res = [4, 3, 2, 0, 1, 0]
    print(s.countSmaller(nums))
