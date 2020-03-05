from typing import List


class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


if __name__ == '__main__':
    nums = [1, 3, 5]
    s = NumArray(nums)

    print(s.sumRange(0, 2))
    s.update(1, 2)
    print(s.sumRange(0, 2))
