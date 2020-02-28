class Solution:

    def isPrime(self, N):
        if N < 2:
            return False
        for i in range(2, int(N ** (1.0 / 2.0)) + 1):
            if (N / i).is_integer():
                return False
        return True

    def isPalindrome(self, N):
        st = str(N)

        for i in range(0, int(len(st) / 2)):
            if st[i] != st[len(st) - i - 1]:
                return False
        return True

    def get_left_right(self, st):
        right = int(len(st) / 2)
        if right == len(st) / 2:
            left = right - 1
        else:
            left = right
        return left, right

    def increase_middle(self, st):
        mid_left, mid_right = self.get_left_right(st)

        self.propagate_increase(st, mid_left, mid_right)

        return st

    def propagate_increase(self, st, left, right):

        new_num = int(st[left]) + 1
        if new_num<10:
            st[left] = str(new_num)
            st[right] = str(new_num)
        else:
            st[left] = '0'
            st[right] = '0'
            return self.propagate_increase(st, left-1, right+1)

    def next_palindrome(self, N):

        st = list(str(N))
        if not self.isPalindrome(N):
            left, right = self.get_left_right(st)

            while left >= 0:
                if st[left] != st[right]:
                    if int(st[left]) < int(st[right]):
                        st = self.increase_middle(st)
                    st[right] = st[left]
                left -= 1
                right += 1

            return int(''.join(st))
        else:
            return N

    def increase_palindrome(self, st, left, right):
        if left < 0:
            return '1' + st[0:-1] + '1'
        num = int(st[left])
        if num < 9:
            if left == right:
                return st[:left] + str(num+1) + st[right + 1:]
            else:
                return st[:left] + str(num+1) + st[left+1:right] + str(num+1) + st[right + 1:]
        else:
            if left == right:
                st = st[:left] + "0" + st[right + 1:]
            else:
                st = st[:left] + "0" + st[left+1:right] + "0" + st[right + 1:]
            return self.increase_palindrome(st, left - 1, right + 1)

    def primePalindrome(self, N: int) -> int:
        N = self.next_palindrome(N)

        while True:
            if self.isPrime(N):
                return N

            st = str(N)
            left = int(len(st) / 2) - 1
            if (len(st) / 2).is_integer():
                right = left + 1
            else:
                left = left + 1
                right = left
            N = int(self.increase_palindrome(st, left, right))


if __name__ == '__main__':
    s = Solution()

    n = 13

    # n = 1
    #
    # n = 9989900
    # n = 9999999
    # n = 10000001
    # print(s.next_palindrome(n))
    n = 102
    # n = 13
    print(s.primePalindrome(n))
