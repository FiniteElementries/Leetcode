# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def insert_node(self, l1, l2, current):

        if l1 is None and l2 is not None:
            current.next = l2
            l2 = l2.next
        elif l1 is not None and l2 is None:
            current.next = l1
            l1 = l1.next
        elif l1.val > l2.val:
            current.next = l2
            l2 = l2.next
        else:
            current.next = l1
            l1 = l1.next
        return current.next, l1, l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        place_holder = ListNode(0)

        head = place_holder
        while l1 is not None or l2 is not None:
            head, l1, l2 = self.insert_node(l1, l2, head)
        return place_holder.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()

    s.mergeTwoLists(l1, l2)