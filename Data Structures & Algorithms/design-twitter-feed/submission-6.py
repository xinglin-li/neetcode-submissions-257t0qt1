class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list) # userId -> list of (time, tweetId)
        self.follow_map = defaultdict(set) # userId -> set of followeeIds  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        # append the newest tweet to user's tweet list
        self.tweet_map[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        followees = self.follow_map[userId] | {userId}

        for followee_id in followees:
            tweets = self.tweet_map[followee_id]
            if tweets:
                idx = len(tweets) - 1
                time, tweet_id = tweets[idx]
                heapq.heappush(max_heap, (-time, tweet_id, followee_id, idx))

        while max_heap and len(res) < 10:
              neg_time, tweet_id, followee_id, idx = heapq.heappop(max_heap)
              res.append(tweet_id)
              if idx > 0:
                next_idx = idx - 1
                time, next_tweet_id = self.tweet_map[followee_id][next_idx]
                heapq.heappush(max_heap, (-time, next_tweet_id, followee_id, next_idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

