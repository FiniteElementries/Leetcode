class Solution:

    def next_pre(self, s, i):
        for j in range(i, len(s)):
            if 'a' <= s[j] <= 'z' or '0' <= s[j] <= '9':
                return j
        return -1

    def next_post(self, s, i):
        for j in range(i, -1, -1):
            if 'a' <= s[j] <= 'z' or '0' <= s[j] <= '9':
                return j
        return -1

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        if not s:
            return True

        l = self.next_pre(s, 0)
        r = self.next_post(s, len(s) - 1)

        while l < r:
            if l * r < 0:
                return False
            if s[l] != s[r]:
                return False
            l = self.next_pre(s, l + 1)
            r = self.next_post(s, r - 1)
        return True


if __name__ == '__main__':
    s = Solution()

    st = "A man, a plan, a canal: Panama"
    # st = "race a car"
    print(s.isPalindrome(st))
