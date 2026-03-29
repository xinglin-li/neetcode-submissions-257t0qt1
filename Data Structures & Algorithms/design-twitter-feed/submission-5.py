from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)   # userId -> set of followeeIds
        self.tweets = defaultdict(list)     # userId -> list of (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        users = set(self.following[userId])
        users.add(userId)   # user should always see their own tweets

        # push each user's most recent tweet into heap
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                # Python heapq is min-heap, so use -time for max-heap behavior
                heapq.heappush(heap, (-time, tweetId, uid, idx - 1))

        while heap and len(res) < 10:
            neg_time, tweetId, uid, next_idx = heapq.heappop(heap)
            res.append(tweetId)

            if next_idx >= 0:
                time, next_tweetId = self.tweets[uid][next_idx]
                heapq.heappush(heap, (-time, next_tweetId, uid, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
