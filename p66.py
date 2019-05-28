from typing import List

class Solution:

    def plugOneDigit(self, i, digits):
        if i==-1:
            return [1] + digits
        else:
            tmp = digits[i] + 1
            if tmp >=10:
                digits[i] = tmp - 10
                return self.plugOneDigit(i-1, digits)
            else:
                digits[i] = tmp
                return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plugOneDigit(len(digits)-1, digits)

if __name__ == "__main__":
    s = Solution()

    digits = [1,2,3]
    digits = [4,3,2,1]
    digits = [9]
    print(s.plusOne(digits))