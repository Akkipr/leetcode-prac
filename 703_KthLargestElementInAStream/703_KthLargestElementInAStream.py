"""
Problem Link : https://leetcode.com/problems/kth-largest-element-in-a-stream/
Platform     : LeetCode
Difficulty   : Easy
"""

import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.party = nums
        if (k > len(self.party)):
            self.ok = self.party
        else:
            for i in range(len(nums)):
                nums[i] = -nums[i]
            self.party = nums
            heapq.heapify(self.party)
            self.ok = []
            for i in range(k):
                self.ok.append(-self.party[i])
            heapq.heapify(self.ok)
        self.counter = k

    def add(self, val: int) -> int:

        heapq.heappush(self.ok, val)
        if len(self.ok) > self.counter:
            heapq.heappop(self.ok)
        print(self.ok)
        x = heapq.heappop(self.ok)
        heapq.heappush(self.ok, x)
        return x
            

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
