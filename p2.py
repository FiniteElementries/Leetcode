"""
https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def carry_node(self, node):
        if node.val >= 10:
            node.val -= 10
            if node.next is None:
                node.next = ListNode(1)
            else:
                node.next.val += 1
            self.carry_node(node.next)

    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)

        current = root
        while l1 is not None or l2 is not None:

            if current.next is None:
                current.next = ListNode(0)

            # if one of the linked list is finished connect the rest of others directly
            # and finish
            end_node = None
            if l1 is None:
                end_node = l2
            elif l2 is None:
                end_node = l1

            if end_node is not None:
                end_node.val += current.next.val
                current.next = end_node
            else:
                current.next.val = current.next.val + l1.val + l2.val

            self.carry_node(current.next)

            if end_node is not None:
                return root.next

            current = current.next
            l1 = l1.next
            l2 = l2.next

        return root.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# l1 = ListNode(1)
# l1.next = ListNode(8)
# l2 = ListNode(0)

l1 = ListNode(0)
l2 = ListNode(0)

l1 = ListNode(9)
l1.next = ListNode(8)
l2 = ListNode(1)

s = Solution()
t = s.addTwoNumbers(l1, l2)

while t is not None:
    print(t.val)
    t = t.next