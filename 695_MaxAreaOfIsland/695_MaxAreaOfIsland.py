"""
Problem Link : https://leetcode.com/problems/max-area-of-island/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0
        self.test_len = 0
        row, col = len(grid), len(grid[0])

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= row or c >= col):
                return
            
            if grid[r][c] == 1:
                self.test_len += 1
                grid[r][c] = 0
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 1):
                    dfs(i,j)
                    if self.test_len > max_len:
                        max_len = self.test_len
                    self.test_len = 0
        return max_len
        
