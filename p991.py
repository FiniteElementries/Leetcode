class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:

        count = 0
        while Y > X:
            if Y % 2 == 0:
                Y /= 2
                count += 1
            else:
                Y += 1
                count += 1
        return int(count + X - Y)


if __name__ == '__main__':
    s = Solution()

    X = 1024
    Y = 1

    print(s.brokenCalc(X, Y))
