import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.following.get(userId, set())
        followees.add(userId)

        for u in followees:
            if u in self.tweets and self.tweets[u]:
                time, tweetId = self.tweets[u][-1]
                idx = len(self.tweets[u]) - 1
                heapq.heappush(heap, (time, tweetId, u, idx))
        res = []
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx - 1 >= 0:
                idx -= 1
                ntime, ntweet = self.tweets[u][idx]
                heapq.heappush(heap, (ntime, ntweet, u, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
