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

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        followees = self.followees[userId]
        followees.add(userId)

        news_feed = []
        for followee in followees:
            news_feed.extend(self.tweets[followee][-10::])
        news_feed.sort(reverse=True)
        return [item[1] for item in news_feed[0:10]]

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

    for action, data in zip(actions, datas):
        if action == "postTweet":
            s.postTweet(data[0], data[1])
        elif action == "getNewsFeed":
            print(s.getNewsFeed(data[0]))

