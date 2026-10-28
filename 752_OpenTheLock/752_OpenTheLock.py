"""
Problem Link : https://leetcode.com/problems/open-the-lock/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        q = deque()
        q.append(["0000", 0])

        def children(node):
            res = []
            for i in range(4):
                digit = str((int(node[i])+1)%10)
                res.append(node[:i] + digit + node[i+1:])
                digit = str(((int(node[i])-1)+10)%10)
                res.append(node[:i] + digit + node[i+1:])
            return res
        
        while q:
            string, turn = q.popleft()
            if string == target:
                return turn
            for stuff in children(string):
                if stuff not in visited:
                    q.append([stuff,turn+1])
                    visited.add(stuff)
        return -1





        
