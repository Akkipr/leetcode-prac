"""
Problem Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1

        while nums[left] > nums[right]:
            middle = (left+right)//2
            if (nums[middle] < nums[right]):
                right = middle
            elif (nums[middle] > nums[right]):
                left = middle + 1
        
        return nums[left]

        '''
        [6,0,1,2,3,4,5]
        [5,6,0,1,2,3,4]
        [4,5,6,0,1,2,3]
        [3,4,5,6,0,1,2]
        [2,3,4,5,6,0,1]
        [1,2,3,4,5,6,0]



        [0,1,2,3,4,5,6]
        '''

