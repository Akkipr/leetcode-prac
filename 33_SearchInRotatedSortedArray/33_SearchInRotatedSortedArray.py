"""
Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while nums[left] > nums[right]:
            middle = (left+right)//2

            if (nums[middle] == target):
                return middle
            elif (nums[middle] > nums[right]):
                if (target < nums[middle]):
                    left = middle
                else:
                    right = middle
            elif (nums[middle] < nums[right]):
                if (target > nums[middle]):
                    left = middle
                else:
                    right = middle
            
            print(nums[left])
            print(nums[right])
        
        return -1


