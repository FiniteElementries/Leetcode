from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followees = defaultdict(set)  # dict of lists
        self.tweets = defaultdict(list)  # dict of lists

        self.tweets_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.tweets_count, tweetId))
        self.tweets_count += 1

    def _add_latest_tweet(self, followee, followee_pointer, heap):
        if followee_pointer[followee] >= 0:
            followee_tweets = self.tweets[followee]
            latest_tweet = followee_tweets[followee_pointer[followee]]
            heapq.heappush(heap, (-latest_tweet[0], followee, latest_tweet[1]))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        followees = self.followees[userId]
        followees.add(userId)

        followee_pointer = {}

        for followee in followees:
            followee_pointer[followee] = len(self.tweets[followee]) - 1

        heap = []
        for followee in followees:
            self._add_latest_tweet(followee, followee_pointer, heap)

        res = []

        while len(heap) > 0 and len(res) < 10:
            latest_tweet = heapq.heappop(heap)
            res.append(latest_tweet[2])

            followee = latest_tweet[1]
            followee_pointer[followee] -= 1
            self._add_latest_tweet(followee, followee_pointer, heap)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == '__main__':
    s = Twitter()

    actions = ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
               "postTweet",
               "postTweet", "postTweet", "postTweet", "getNewsFeed"]
    datas = [[], [1, 5], [1, 3], [1, 101], [1, 13], [1, 10], [1, 2], [1, 94], [1, 505], [1, 333], [1, 22], [1, 11], [1]]

    actions = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    datas = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

    for action, data in zip(actions, datas):
        if action == "postTweet":
            s.postTweet(data[0], data[1])
            print(None)
        elif action == "follow":
            s.follow(data[0], data[1])
            print(None)
        elif action == 'unfollow':
            s.unfollow(*data)
            print(None)
        elif action == "getNewsFeed":
            print(s.getNewsFeed(data[0]))
