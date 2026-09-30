"""
Problem Link : https://leetcode.com/problems/koko-eating-bananas/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            
            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2

            if (works(middle)):
                right = middle
            else:
                left = middle + 1
        
        return right
        
