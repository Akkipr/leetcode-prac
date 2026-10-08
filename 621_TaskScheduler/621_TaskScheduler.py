"""
Problem Link : https://leetcode.com/problems/task-scheduler/
Platform     : LeetCode
Difficulty   : Medium
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord('A')] += 1

        max_freq = max(counts)
        num_max = counts.count(max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)
