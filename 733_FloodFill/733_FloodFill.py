"""
Problem Link : https://leetcode.com/problems/flood-fill/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num = image[sr][sc]

        if num == color:
            return image

        row, col = len(image), len(image[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=row or c>=col):
                return
            
            if image[r][c] == num:
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        dfs(sr,sc)
        return image

