from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for s in strs:
            if s=="":
                return ""
        if len(strs) == 1:
            return strs[0]

        i = 0
        match = True
        while match:
            for j in range(len(strs) - 1):
                if i >= len(strs[j]) or i >= len(strs[j + 1]):
                    match = False
                    break
                if strs[j][i] != strs[j + 1][i]:
                    match = False
                    break
            if match:
                i+=1

        if i == 0:
            return ""
        else:
            return strs[0][0:i]


if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))
