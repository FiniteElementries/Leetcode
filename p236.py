# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def dfs(self, node):
        if self.lca:
            return 0
        if not node:
            return 0

        if node.val in self.s:
            count = 1
        else:
            count = 0
        count += self.dfs(node.left)
        count += self.dfs(node.right)

        if count == 2:
            self.lca = node
            return 0
        else:
            return count

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.s = {p.val, q.val}
        self.lca = None
        self.dfs(root)

        return self.lca


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


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    try:
        line = "[3,5,1,6,2,0,8,null,null,7,4]"
        root = stringToTreeNode(line)
        line = "8"
        p = TreeNode(5)
        line = "4"
        q = TreeNode(4)

        ret = Solution().lowestCommonAncestor(root, p, q)

        out = treeNodeToString(ret)
        print(ret.val)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
