# Last updated: 5/13/2026, 1:14:19 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        new_array = [0,0]

        while (i < j):
            if (numbers[i] + numbers[j] == target):
                new_array[0] = i+1
                new_array[1] = j+1
                print(new_array)
                return new_array
            elif (numbers[i] + numbers[j] > target):
                j-=1
            else:
                i+=1
        