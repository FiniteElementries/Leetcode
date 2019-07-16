# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        seta = set([])
        setb = set([])

        while headA or headB:
            if headA:
                if headA in setb:
                    return headA
                else:
                    seta.add(headA)
                    headA = headA.next

            if headB:
                if headB in seta:
                    return headB
                else:
                    setb.add(headB)
                    headB = headB.next
        return None
