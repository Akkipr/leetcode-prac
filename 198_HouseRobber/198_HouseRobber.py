"""
Problem Link : https://leetcode.com/problems/house-robber/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0

        for i in range(len(nums)):
            cur = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = cur
        
        return rob2







        '''
        arr = {}

        def dp(i):
            if i >= len(nums):
                return 0
            if i in arr:
                return arr[i]
            
            arr[i] = max(dp(i+1), nums[i]+dp(i+2))
            return arr[i]
        
        return dp(0)
        '''
        
