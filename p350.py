

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        retVal = []
        for i in nums1:
            if (i in nums2):
                retVal.append(i)
                nums2.remove(i)

        return retVal



if __name__=="__main__":
    s = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2]

    print(s.intersect(nums1, nums2))

