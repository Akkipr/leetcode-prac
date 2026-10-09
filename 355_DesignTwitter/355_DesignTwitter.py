"""
Problem Link : https://leetcode.com/problems/design-twitter/
Platform     : LeetCode
Difficulty   : Medium
"""

import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetIDMap = {None:None}
        self.followers = {None:None}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetIDMap:
            self.tweetIDMap[userId] = []
        self.tweetIDMap[userId].append([-self.count,tweetId])
        self.count +=1
        

    def getNewsFeed(self, userId: int) -> list[int]:
        min_heap = []
        feed = []

        # Include yourself and everyone you follow
        users = self.followers.get(userId, set()).copy()
        users.add(userId)

        # Add each user's newest tweet
        for followeeID in users:
            tweets = self.tweetIDMap.get(followeeID, [])

            if tweets:
                index = len(tweets) - 1
                count, tweetID = tweets[index]

                heapq.heappush(
                    min_heap,
                    (count, tweetID, followeeID, index)
                )

        # Keep popping the newest tweet
        while min_heap and len(feed) < 10:
            count, tweetID, followeeID, index = heapq.heappop(min_heap)
            feed.append(tweetID)

            # Add the next older tweet from the same user
            index -= 1

            if index >= 0:
                count, tweetID = self.tweetIDMap[followeeID][index]

                heapq.heappush(
                    min_heap,
                    (count, tweetID, followeeID, index)
                )

        return feed


        
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            return
        
        self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
