# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def dfs(self, node, k):


        if node is None:
            return False

        if node.left is None and not self.counting:
            self.counting = True

        if self.dfs(node.left, k):
            return True
        self.count += 1
        if self.count >= k:
            self.val = node.val
            return True
        if self.dfs(node.right, k):
            return True

        return False

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.counting = False
        self.count = 0
        self.val = None

        self.dfs(root, k)

        return self.val


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')


    line = "[41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, null, 43, 46, 49, 0, 2, 30, 36, null, null, null, null, \
            null, null, 45, 47, null, null, null, null, null, 4, 29, 32, null, null, null, null, null, null, 3, \
            9, 26, null, 31, 34, null, null, 7, 11, 25, 27, null, null, 33, null, 6, 8, 10, 16, null, null, \
            null, 28, null, null, 5, null, null, null, null, null, 15, 19, null, null, null, null, 12, null, 18, \
            20, null, 13, 17, null, null, 22, null, 14, null, null, 21, 23]"
    root = stringToTreeNode(line)

    k = stringToInt(25)

    ret = Solution().kthSmallest(root, k)

    out = intToString(ret)

    print(out)


if __name__ == '__main__':
    main()
