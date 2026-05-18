# Last updated: 5/18/2026, 4:34:55 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        summ=0

        while (l < r):
            current_height = min(height[l], height[r])
            length = r-l
            temp_sum = length*current_height
            if (temp_sum > summ):
                summ=temp_sum

            if (height[l] <= height[r]):
                l+=1
            elif (height[l] > height[r]):
                r=r-1
        return summ
        
