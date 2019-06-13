"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    node_map = {}

    def get_node(self, old_node):
        if old_node is None:
            return None
        if old_node not in self.node_map:
            self.node_map[old_node] = Node(old_node.val, None, None)
            self.node_map[old_node].next = self.get_node(old_node.next)
            self.node_map[old_node].random = self.get_node(old_node.random)
        return self.node_map[old_node]

    def copyRandomList(self, head: 'Node') -> 'Node':

        self.node_map = {}
        copy_head = self.get_node(head)
        new_node = copy_head
        while head is not None:
            if new_node.next is None:
                new_node.next = self.get_node(head.next)
            head = head.next
            new_node = copy_head.next

        return copy_head


if __name__ == "__main__":

    head = Node(1, None, None)
    n2 = Node(2, None, None)

    head.next = n2
    head.random = n2

    n2.random = n2

    s = Solution()

    cop = s.copyRandomList(head)

    print(cop)