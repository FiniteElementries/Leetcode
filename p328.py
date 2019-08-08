# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        n = 1
        even = None
        odd = None
        even_head = None
        odd_head = None
        while head:
            if n % 2 == 0:
                if not even:
                    even = head
                    even_head = even
                else:
                    even.next = head
                    even = head
            else:
                if not odd:
                    odd = head
                    odd_head = odd
                else:
                    odd.next = head
                    odd = head
            n+=1
            head = head.next
        if even:
            even.next = None
        odd.next = even_head
        return odd_head


if __name__ == '__main__':

    s = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    new_head = s.oddEvenList(head)

    print(new_head)