# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head

        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        arr.reverse()

        node = head
        i = 0
        while i < len(arr) / 2:
            if node.val != arr[i]:
                return False
            node = node.next
            i += 1
        return True
