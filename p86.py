# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        less_head = None
        more_head = None
        less_node = None
        more_node = None

        while head is not None:
            if head.val < x:
                if not less_node:
                    less_head = head
                    less_node = head
                else:
                    less_node.next = head
                    less_node = head
            else:
                if not more_node:
                    more_head = head
                    more_node = head
                else:
                    more_node.next = head
                    more_node = head
            head = head.next
        if less_node:
            less_node.next = more_head
        more_node.next = None

        return less_head if less_head else more_head
