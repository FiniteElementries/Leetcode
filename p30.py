from collections import Counter
from typing import List


class Solution:

    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += 1

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not words:
            return []

        self.len_word = len(words[0])
        self.total_length = self.len_word * len(words)
        lookup_table = {}
        # create lookup table
        for word in set(words):
            for ind in self.find_all(s, word):
                if ind not in lookup_table:
                    lookup_table[ind] = set()
                lookup_table[ind].add(word)

        res = []
        c = Counter(words)
        for i in range(0, len(s) - len(words) * len(words[0]) + 1):
            if self.lookup_word(lookup_table, c, i, i, s):
                res.append(i)

        return res

    def lookup_word(self, table, words, start_ind, ind, s):

        if start_ind + self.total_length == ind:
            return True

        if ind not in table:
            return False
        table_entries = table[ind]

        for item in table_entries:
            if item in words and words[item] > 0:
                words[item] -= 1
                if self.lookup_word(table, words, start_ind, ind + len(item), s):
                    words[item] += 1
                    return True
                words[item] += 1
        return False


if __name__ == '__main__':
    s = Solution()

    st = "barfoothefoobarman"
    words = ["foo", "bar"]

    # st = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "good"]

    print(s.findSubstring(st, words))
