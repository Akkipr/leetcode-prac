# Last updated: 5/11/2026, 8:51:17 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if (len(nums)> 1) :
            left_arr = nums[:len(nums) // 2] 
            right_arr = nums[len(nums) // 2:]

            self.sortArray(left_arr)
            self.sortArray(right_arr)

            i=0
            j=0
            k=0
            while (i < len(left_arr) and j < len(right_arr)):
                if (left_arr[i] < right_arr[j]):
                    nums[k] = left_arr[i]
                    i+=1
                else:
                    nums[k] = right_arr[j]
                    j+=1
                k+=1

            while (i < len(left_arr)):
                nums[k] = left_arr[i]
                i+=1
                k+=1
            while (j < len(right_arr)):
                nums[k] = right_arr[j]
                j+=1
                k+=1
            
        return nums



    '''
    Attempt 2: Use QuickSort - costly in memory
        if len(nums) <= 1:
            return nums
        
        pivot = nums[len(nums) // 2]  
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        return self.sortArray(left) + middle + self.sortArray(right)
    '''
    '''
    Attempt #1 with modified Insertion sort
    for i in range(1,len(nums)):
        if (nums[i] > nums[i-1]):
            continue         
        key = nums[i]
        j= i-1

        while (j>=0 and nums[j] > key):
            nums[j+1] = nums[j]
            j = j-1
        nums[j+1] = key

    return nums
        '''
        