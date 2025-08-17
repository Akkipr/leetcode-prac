# Last updated: 8/17/2025, 12:37:28 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newarray=[0,0]
        counter=0
        counter1=1
        for i in range(len(nums)):
            for j in range(counter1,len(nums)):
                if (nums[i]+nums[j]==target):
                    newarray[0]=i
                    newarray[1]=j
                if ((len(nums)-1) == j):
                    counter1+=1
        return newarray
        
        