"""
Problem Link : https://leetcode.com/problems/climbing-stairs/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n+1):
            memo[i] = memo[i-2] + memo[i-1]
                
        return memo[n]
        

