class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = list(format(n, '032b'))
        mid = len(b)//2
        for i in range(0, mid):
            tmp = b[-(i+1)]
            b[-(i+1)] = b[i]
            b[i] = tmp

        return int(''.join(b), 2)


if __name__ == '__main__':

    s = Solution()

    n = 43261596


    print(s.reverseBits(n))


