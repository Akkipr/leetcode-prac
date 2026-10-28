"""
Problem Link : https://leetcode.com/problems/number-of-provinces/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city: int):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                dfs(i)
                
        return provinces

