"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import sys

        if(divisor==0):
            import sys
            return sys.maxint


        sign = 1
        if(dividend<0):
            sign = sign * (-1)
            dividend = -dividend

        if(divisor<0):
            sign = sign * (-1)
            divisor = -divisor

        if(divisor>dividend):
            return 0

        sum = 0
        ratio = 0
        while(True):
            step = 0
            ratio_step = 0

            while(sum<=dividend):
                sum = sum + step + divisor
                step = step + divisor

                ratio = ratio + ratio_step + 1
                ratio_step = ratio_step + 1

            if(step==divisor):
                break
            else:
                sum = sum - step
                ratio = ratio - ratio_step


        retVal = (ratio-1) * sign

        if(retVal<-2147483648 or retVal > 2147483647):
            return 2147483647

        return retVal



if __name__=="__main__":

    dividend = -2147483648
    divisor = -1

    solution = Solution()
    print(solution.divide(dividend, divisor))