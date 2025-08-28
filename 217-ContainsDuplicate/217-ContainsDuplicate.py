# Last updated: 8/28/2025, 2:00:30 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if (num in s):
                return True
            else:
                s.add(num)

        return False



        '''
        Old Solution (More runttime memory)

        What I learned:
        HashSets are a LOT faster than arrays! 
        
        nums.sort()
        for i in range (len(nums)-1):
            if (nums[i]==nums[i+1]):
                return True
        return False
        '''
