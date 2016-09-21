class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        wordDict = list(wordDict)
        wordDict.sort(key=len, reverse=True)
        self.dict = wordDict

        return self.find_word(s)

    def find_word(self, s):

        for word in self.dict:

            if(len(word) > len(s)):
                continue

            sub_str = s.split(word)

            if(len(sub_str)==1): # word not in string
                continue

            finished = [True]
            for item in sub_str: # word in string, look into sub string
                if(item!=""):
                    finished.append(self.find_word(item))

            if(False not in finished):
                return True

        return False


if __name__=="__main__":

    sol = Solution()

    s = "leetcode"
    dict = {"leet", "code"}

    print(sol.wordBreak(s, dict))

    s = "cars"
    dict = {"car", "ca","rs"}

    print(sol.wordBreak(s, dict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    dict = {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}

    print(sol.wordBreak(s, dict))

    s = "acccbccb"
    dict = {"cc","bc","ac","ca"}
    print(sol.wordBreak(s, dict))


    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dict = {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}

    print(sol.wordBreak(s, dict))