from typing import List


class Solution:
    ret_val = []

    def dfs(self, palindrome_map, cuts, s):
        if cuts[-1] == len(s):
            val = []
            for i in range(0, len(cuts) - 1):
                val.append(s[cuts[i]:cuts[i + 1]])
            self.ret_val.append(val)
            return

        for v in palindrome_map[cuts[-1]]:

            self.dfs(palindrome_map, cuts + [v+1], s)

    def partition(self, s: str) -> List[List[str]]:
        self.ret_val = []
        queue = []
        for i in range(0, len(s)):
            queue.append([i, i])

        palindrome_map = {}
        while len(queue) > 0:
            pd = queue.pop()

            l = pd[0]
            r = pd[1]

            if l not in palindrome_map:
                palindrome_map[l] = set([])
            palindrome_map[l].add(r)

            if l == r:
                if l > 0:
                    if s[l - 1] == s[l]:
                        queue.append([l - 1, r])
                if r < len(s) - 1:
                    if s[r + 1] == s[r]:
                        queue.append([l, r + 1])
            if 0 < l <= r < len(s) - 1:
                if s[l - 1] == s[r + 1]:
                    queue.append([l - 1, r + 1])

        self.dfs(palindrome_map, [0], s)

        return self.ret_val


if __name__ == "__main__":
    s = Solution()

    st = 'aab'

    st = 'efe'
    print(s.partition(st))
