"""
Problem Link : https://leetcode.com/problems/search-a-2d-matrix/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m*n) - 1
        
        while left <= right:
            middle = (left+right) // 2
            row = middle // n
            col = middle % n

            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                left = middle + 1
            else:
                right = middle -1
        
        return False
