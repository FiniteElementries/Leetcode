"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:

    def get_ind(self, c):
        return ord(c) - 97

    def lengthOfLongestSubstring(self, s):

        ls = []
        current_min = 0
        tracker = [-1] * 26

        for i in range(0, len(s)):

            k = self.get_ind(s[i])

            # this char is not encountered
            if tracker[k] == -1:
                tracker[k] = i
            else:

                # encountered char, get previous index
                pre_ind = tracker[k]
                tracker[k] = i  # set new tracker position

                # from current min to i should be the not repeated char
                ls.append(i - current_min)

                # update current min to the one after last counter of this character
                current_min = max(current_min, pre_ind + 1)

        ls.append(len(s) - current_min)

        return max(ls)



s = Solution()

print(s.lengthOfLongestSubstring(""))