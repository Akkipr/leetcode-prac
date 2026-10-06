"""
Problem Link : https://leetcode.com/problems/last-stone-weight/
Platform     : LeetCode
Difficulty   : Easy
"""

import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify(stones)



        while len(stones) != 1:
            leftover = []
            while len(stones) != 2:
                heapq.heappush(leftover, heapq.heappop(stones))
            difference = abs(stones[0]-stones[1])
            stones = leftover
            if (difference != 0):
                heapq.heappush(stones,difference)
        
        return stones[0]
            
        
