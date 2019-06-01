from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = {}

        for s in strs:
            s2 = ''.join(sorted(s))
            if s2 not in mapping:
                mapping[s2] = []

            mapping[s2].append(s)

        return list(mapping.values())


if __name__ == "__main__":
    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(s.groupAnagrams(strs))