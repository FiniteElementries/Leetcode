import math


class Solution:

    def set_not_prime(self, i, is_prime):
        j = i * 2
        while j < len(is_prime):
            is_prime[j] = False
            j += i

    def isPrime(self, n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                if self.isPrime(i):
                    self.set_not_prime(i, is_prime)
                else:
                    is_prime[i] = False
        count = 0
        for item in is_prime:
            if item:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()

    n = 499979
    # n = 10
    n = 999983
    n = 10
    # n = 4
    # n = 2
    # n  = 3
    print(s.countPrimes(n))
