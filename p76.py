from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        missing = len(t)

        j = 0
        start = 0
        end = 0

        for i in range(0, len(s)):
            if s[i] in need:
                need[s[i]] -= 1
                if need[s[i]] >= 0:
                    missing -= 1

            if missing == 0:
                while j <= i:
                    if s[j] in need:
                        need[s[j]] += 1
                        if need[s[j]] > 0:
                            missing += 1
                            if missing > 0:
                                if i - j < end - start or end == 0:
                                    start = j
                                    end = i + 1
                                j += 1
                                break
                    j += 1

        return s[start:end]


if __name__ == "__main__":
    s = Solution()

    S = "a"
    T = "aa"

    S = "ADOBECODEBANC"
    T = "AABC"
    #
    S = "ADOBECODEBANC"
    T = "AABFC"
    # #
    # S = 'aa'
    # T = 'aa'

    S = "ADOBECODEBANC"
    T = "ABC"

    # S = "ab"
    # T = "a"

    print(s.minWindow(S, T))
