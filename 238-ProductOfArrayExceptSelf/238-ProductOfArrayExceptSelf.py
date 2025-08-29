# Last updated: 8/28/2025, 8:39:20 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        new_num = 0


        for i in range(len(nums)):
            if i==0:
                prefix_array.append(1)
                new_num = nums[i]
            else:
                prefix_array.append(new_num)
                new_num = new_num*nums[i]

        new_num = 0

        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                new_nums = nums[j]
            else:
                prefix_array[j]= prefix_array[j]*new_nums
                new_nums = new_nums*nums[j]
    
        
        return prefix_array






        