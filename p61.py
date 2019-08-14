# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        count = 0
        node = head
        while node is not None:
            pre_node = node
            node = node.next
            count += 1
        pre_node.next = head

        new_head = head

        for i in range(count - k % count):
            pre_node = new_head
            new_head = new_head.next

        pre_node.next = None

        return new_head
