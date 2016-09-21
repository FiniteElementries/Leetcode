import heapq
import numpy as np

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if(len(nums1) == 0 or len(nums2) == 0):
            return []

        m = len(nums1)
        n = len(nums2)


        retVal = []

        if(k>= m * n):
            for i in range(0, m):
                for j in range(0, n):
                    retVal.append([nums1[i], nums2[j]])
            return  retVal

        sum = np.array([nums1,] * n) + np.array([nums2,] * m).transpose()



        heap_list = []



        for i in range(0, len(sum[0])):
            heap_list.append(Heap(0, i, sum[0][i]))

        for i in range(0, min(k, sum.size)):
            min_heap, ind = find_min_heap(heap_list)

            retVal.append([nums1[min_heap.j], nums2[min_heap.i]])

            if(min_heap.i + 1 < n):
                heap_list[ind] = Heap(min_heap.i + 1, min_heap.j, sum[min_heap.i + 1][min_heap.j])
            else:
                del heap_list[ind]


        return retVal

class Heap():
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val


def find_min_heap(heap_list):
    min_heap = heap_list[0]
    ind = 0

    for i in range(0, len(heap_list)):

        if(min_heap.val > heap_list[i].val):

            min_heap = heap_list[i]
            ind = i

    return min_heap, ind



if __name__=="__main__":

    sol = Solution()

    nums1 = [1,7,11,13]
    nums2 = [2,4,6]
    k=3

    print(sol.kSmallestPairs(nums1, nums2, k))

    nums1 = [1]
    nums2 = [3,5,6,7,8,100]
    k=4

    print(sol.kSmallestPairs(nums1, nums2, k))

    nums1 = [0,0,0,0,0]
    nums2 = [-3,22,35,56,76]
    k=22

    print(sol.kSmallestPairs(nums1, nums2, k))

