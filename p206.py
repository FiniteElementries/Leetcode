
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, node, pre_node):
        if node is None:
            return pre_node
        n = node.next
        node.next = pre_node
        return self.reverse(n, node)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
