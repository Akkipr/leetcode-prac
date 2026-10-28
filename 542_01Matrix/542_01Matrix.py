"""
Problem Link : https://leetcode.com/problems/01-matrix/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        if not mat or not mat[0]:
            return
        
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    queue.append((r, c))
                    mat[r][c] = "S"

        print(queue)
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            test = 0
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] != "S":
                    num = mat[nr][nc]+1
                    if not isinstance(mat[r][c], str):
                        if num > mat[r][c]:
                            num = mat[r][c]
                    mat[r][c] = num
                        
            if mat[r][c] == "S":
                queue.append((r,c))
            

        return mat

        
