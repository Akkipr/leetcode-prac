"""
Problem Link : https://leetcode.com/problems/rectangle-overlap/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1 is None or rec2 is None:
            return False

        if (rec1[0] > rec2[0] and rec1[1] > rec2[1]):
            # rec1 is the lower half
            if rec2[0] >= rec1[2] and rec2[1] >= rec1[3]:
                return True
        

        if (rec1[0] < rec2[0] and rec1[1] < rec2[1]):
            # rec2 is the lower half
            if rec2[0] < rec1[2] and rec2[1] < rec1[3]:
                return True
        
        return False


