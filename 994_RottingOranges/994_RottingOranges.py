"""
Problem Link : https://leetcode.com/problems/rotting-oranges/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0,1,2
        m,n = len(grid), len(grid[0])
        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == FRESH):
                    num_fresh +=1
                elif (grid[i][j] == ROTTEN):
                    q.append((i,j))
        
        if num_fresh == 0:
            return 0
        
        num_minutes = -1        # final iteration where nothing happens

        while q:
            size = len(q)
            num_minutes +=1
            for _ in range(size):
                i,j = q.popleft()
                for r,c in [(i,j+1), (i+1,j), (i-1,j), (i,j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append((r, c))
        
        # Return the time taken or -1 if fresh oranges remain
        return num_minutes if num_fresh == 0 else -1



