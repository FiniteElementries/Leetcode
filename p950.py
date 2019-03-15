"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/
"""
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        sorted_deck = deck[:]
        sorted_deck.sort(reverse=True)

        que = [sorted_deck[0]]
        for i in range(1, len(sorted_deck)):
            que = [sorted_deck[i]] + [que[-1]] + que[0:-1]

        return que


s = Solution()

print(s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
