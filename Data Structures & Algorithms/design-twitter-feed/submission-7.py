class Twitter:

    def __init__(self):
        self.time = 0 # global timestamp
        self.tweets = defaultdict(list) # userId -> list of (timestamp, tweetId)
        self.followees = defaultdict(set) # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        max_heap = []
        
        # 默认关注自己，才能看到自己的推文
        self.followees[userId].add(userId)
        
        # 多路归并初始化：收集关注列表中每个人的最新一条推文
        # 堆元组含义: (-timestamp, tweetId, followeeId, next_index)
        for followeeId in self.followees[userId]:
            if followeeId in self.tweets and self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1  # 最新推文在末尾
                time, tweetId = self.tweets[followeeId][index]
                max_heap.append((-time, tweetId, followeeId, index - 1))
        
        heapq.heapify(max_heap)
        
        # 最多获取 10 条最新的推文
        while max_heap and len(res) < 10:
            neg_time, tweetId, followeeId, next_index = heapq.heappop(max_heap)
            res.append(tweetId)
            # 如果该用户还有更早的推文，继续放入堆中供后续比较
            if next_index >= 0:
                time, prev_tweetId = self.tweets[followeeId][next_index]
                heapq.heappush(max_heap, (-time, prev_tweetId, followeeId, next_index - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
