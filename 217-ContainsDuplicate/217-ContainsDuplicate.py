# Last updated: 8/28/2025, 1:59:45 AM
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
        nums.sort()
        for i in range (len(nums)-1):
            if (nums[i]==nums[i+1]):
                return True
        return False
        '''