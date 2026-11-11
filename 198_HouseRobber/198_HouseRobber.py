"""
Problem Link : https://leetcode.com/problems/house-robber/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        arr = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in arr:
                return arr[i]
            
            arr[i] = max(dp(i+1), nums[i]+dp(i+2))
            return arr[i]
        
        return dp(0)
        
