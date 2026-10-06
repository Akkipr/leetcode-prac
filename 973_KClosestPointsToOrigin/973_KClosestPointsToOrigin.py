"""
Problem Link : https://leetcode.com/problems/k-closest-points-to-origin/
Platform     : LeetCode
Difficulty   : Medium
"""

import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        complete_array = []
        dictionary = {}
        final_array = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(complete_array, distance)
            dictionary[distance] = point
        
        heapq.heapify(complete_array)
        while k > 0:
            j = heapq.heappop(complete_array)
            final_array.append(dictionary[j])
            k=k-1
        
        return final_array

        
