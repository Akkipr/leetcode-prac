"""
Problem Link : https://leetcode.com/problems/course-schedule-ii/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = defaultdict(list)

        for n, m in prerequisites:
            g[n].append(m)

        UNVISITED, VISITING, VISITED = 0,1,2

        states = [UNVISITED] * numCourses
        totalArr = []

        def dfs(i):
            state = states[i]

            if state == VISITED: 
                return True
            elif state == VISITING:
                return False
            else:
                state = VISITING
                for nei in g[i]:
                    if not dfs(nei):
                        return False
                state = VISITED
                if i not in totalArr:
                    totalArr.append(i)
                return True

                    
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return totalArr

        
