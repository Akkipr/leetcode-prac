"""
Problem Link : https://leetcode.com/problems/is-graph-bipartite/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        odd = [0] * len(graph)

        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if odd[node] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[node]
            return True
                
        for i in range(len(graph)):
            if odd[i] == 0:
                if not bfs(i):
                    return False
        return True
        
