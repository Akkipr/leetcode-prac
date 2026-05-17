# Last updated: 5/16/2026, 8:05:00 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        summ=0

        while (l != len(height)-1):
            while (l < r):
                if (height[l] <= height[r]):
                    length = r-l
                    temp_sum = length*height[l]
                    if (temp_sum > summ):
                        summ=temp_sum
                    break
                elif (height[l] > height[r]):
                    r=r-1
            l+=1
        l=0
        r=len(height)-1

        while (r != 0):
            while (r > l):
                if (height[r] <= height[l]):
                    length = r-l
                    temp_sum = length*height[r]
                    if (temp_sum > summ):
                        summ=temp_sum
                    break
                elif (height[r] > height[l]):
                    l=l+1
            r-=1
        return summ
        