from typing import List


class Solution:

    def locate_pivote(self, nums, i, j):

        if j-i == 1:
            return i, j

        mid = int((i+j)/2)

        if nums[i] < nums[mid] and nums[mid] > nums[j]:
            return self.locate_pivote(nums, mid, j)
        else:
            return self.locate_pivote(nums, i, mid)


    def search_array(self, arr, i, j, val):
        if val > arr[j] or val < arr[i]:
            return -1
        if val == arr[i]:
            return i
        if val == arr[j]:
            return j

        if j - i == 1:
            return -1

        mid = int((i+j)/2)
        if val < arr[mid]:
            return self.search_array(arr, i, mid, val)
        else:
            return self.search_array(arr, mid, j, val)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        i, j = self.locate_pivote(nums, 0, len(nums)-1)

        # if not pivoted:
        #     return self.search_array(nums, i, j, target)

        ind = self.search_array(nums, j, len(nums)-1, target)
        if ind != -1:
            return ind
        else:
            return self.search_array(nums, 0, i, target)



if __name__ == "__main__":
    s = Solution()

    # nums = [4,5,6,7,0,1,2]
    # nums = [1]
    # nums = [3,5,1]
    # nums = [1,2,3,4,5,6]
    # nums = [3,4,5,6,7,1,2]
    # nums = [1, 3]
    # nums = [3, 1]
    nums = [1, 3, 5]
    # nums = [5, 1, 3]
    # nums = [3, 5, 1]
    print(s.search(nums, 1))
    # print(s.search(nums, 1))