# Last updated: 8/28/2025, 1:04:41 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set()

        final_count = [0] * k
        final_set = [0] * k

        current_num = nums[0]
        index = -1


        nums.sort()
        count = [0] * len(nums)
        for j in range(len(nums)):
            if nums[j] in s:
                count[index] = count[index] + 1
            else:
                s.add(nums[j])
                index=index+1
                count[index] = 1

        list_version = list(s)
        list_version.sort()



        p=0
        while p != k:
            for i in range (len(list_version)):
                if (count[i] > final_count[p]):
                    final_set[p] = list_version[i]
                    final_count[p] = count[i]
            list_version.remove(final_set[p])
            count.remove(final_count[p])
            p=p+1
        
        return final_set


            

        
            

                

        