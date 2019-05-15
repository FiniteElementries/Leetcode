from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyHeap(object):
    def __init__(self):
        self._data = []

        self.mapping = {}

    def size(self):
        return len(self._data)

    def push(self, item):
        if item.val not in self.mapping:
            self.mapping[item.val] = []
        self.mapping[item.val].append(item)
        heapq.heappush(self._data, item.val)

    def pop(self):
        val = heapq.heappop(self._data)
        item = self.mapping[val][-1]
        self.mapping[val].pop()
        return item


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = MyHeap()

        for item in lists:
            if item is not None:
                heap.push(item)
        if heap.size() == 0:
            return []

        head = heap.pop()
        current = head
        while heap.size() > 0:
            if current.next is not None:
                heap.push(current.next)

            tmp = heap.pop()
            current.next = tmp
            current = tmp

        return head
