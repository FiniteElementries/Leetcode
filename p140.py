from typing import List


class Solution:

    cache = {}
    def str_after(self, s, i, wordDict, min_l, max_l):
        """ Get all strings after index """

        if i not in self.cache:
            if i >= len(s):
                return []
            words = []
            for j in range(min_l, max_l + 1):
                if s[i:i + j] in wordDict:
                    words.append(s[i:i + j])
            if not words:
                return []

            ret_val = []
            for word in words:
                if i + len(word) == len(s):
                    ret_val.append(word)
                else:
                    words_after = self.str_after(s, i + len(word), wordDict, min_l, max_l)
                    for w in words_after:
                        ret_val.append(f"{word} {w}")

            self.cache[i] = set(ret_val)

        return self.cache[i]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if len(wordDict) == 0:
            return []

        if len(s) == 0:
            return []

        self.cache = {}

        min_l = len(wordDict[0])
        max_l = len(wordDict[0])
        for w in wordDict:
            if len(w) < min_l:
                min_l = len(w)
            if len(w) > max_l:
                max_l = len(w)

        return list(self.str_after(s, 0, set(wordDict), min_l, max_l))


if __name__ == "__main__":
    s = Solution()
    st = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]

    st = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

    st = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(s.wordBreak(st, wordDict))
