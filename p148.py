# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:  # None
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next

        l.sort()

        head = ListNode(l[0])
        node = head
        for item in l[1:]:
            node.next = ListNode(item)
            node = node.next
        return head
