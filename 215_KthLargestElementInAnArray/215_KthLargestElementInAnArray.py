"""
Problem Link : https://leetcode.com/problems/kth-largest-element-in-an-array/
Platform     : LeetCode
Difficulty   : Medium
"""

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        i=0
        target = 0
        while i < k:
            target = heapq.heappop(nums)
            i += 1
        return -target

        
