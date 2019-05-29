class Solution:

    def find_low(self, x):
        orig_x = x
        while x>0:
            x=x//2
            if x**2<=orig_x:
                return x
        return x

    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        lower = self.find_low(x)
        higher = x*2

        for i in range(lower, higher):
            if i*i>x:
                return i-1


if __name__ == "__main__":
    s = Solution()

    x = 2
    print(s.mySqrt(x))
