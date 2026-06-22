class Twitter:

    def __init__(self):
        self.users = defaultdict(deque) #tweets given by the user
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((self.time, tweetId))
        if len(self.users[userId]) > 10:
            self.users[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = []
        for following in self.following[userId]:
            users.append(following)
        users.append(userId)

        last_tweets = []
        for u in users:
            if self.users[u]:
                last_idx = len(self.users[u])-1
                time, tweetId = self.users[u][last_idx]
                heapq.heappush(last_tweets, (-time, tweetId, u, last_idx-1))
        
        res = []
        while last_tweets and len(res)<10:
            time, tweetId, user, next_idx = heapq.heappop(last_tweets)
            res.append(tweetId)
            if next_idx >= 0:
                time, tweetId = self.users[user][next_idx]
                heapq.heappush(last_tweets, (-time, tweetId, user, next_idx-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
