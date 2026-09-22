"""
Problem Link : https://leetcode.com/problems/minimum-moves-to-reach-target-score/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        g = target
        count = 0
        while g > 1:
            if (g%2 == 0 and maxDoubles != 0):
                g = int(g/2)
                maxDoubles-=1
            elif (g%2 == 0 and maxDoubles == 0):
                g=g-1
                count += g
                return count
            else:
                g = g-1
            count+=1
        return count

