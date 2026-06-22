class Twitter:

    def __init__(self):
        self.users = defaultdict(list) #tweets given by the user
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.users[userId], (self.time, tweetId))
        while len(self.users[userId]) > 10:
            heapq.heappop(self.users[userId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = []
        for following in self.following[userId]:
            users.append(following)
        users.append(userId)

        tweets = []
        heapq.heapify(tweets)
        for user in users:
            for tweet in self.users[user]:
                heapq.heappush(tweets, tweet)
                while len(tweets) > 10:
                    heapq.heappop(tweets)
        returned_tweets = []
        while tweets:
            returned_tweets.append(heapq.heappop(tweets)[1])
        returned_tweets.reverse()
        return returned_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
