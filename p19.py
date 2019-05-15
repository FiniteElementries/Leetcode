
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        first = head
        while head is not None:
            nodes.append(head)
            head = head.next

        remove_node = nodes[-n]

        if n == len(nodes):
            return remove_node.next
        else:
            pre_node = nodes[-(n+1)]
            pre_node.next = remove_node.next

            return first