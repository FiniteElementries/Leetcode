from math import sqrt


class Solution:

    def find_squares(self, val):
        if val == 0:
            return 1

        if val not in self.cache:
            sq = int(sqrt(val))

            min_squares = val + 1
            for i in range(sq, sq//2, -1):
                new_val = val - i ** 2
                s = self.find_squares(new_val)
                if s > 0:
                    if s < min_squares:
                        min_squares = s

            res = min_squares + 1
            self.cache[val] = res
        return self.cache[val]

    def numSquares(self, n: int) -> int:
        self.cache = {}
        return self.find_squares(n) - 1


if __name__ == '__main__':
    s = Solution()

    n = 40

    print(s.numSquares(n))
