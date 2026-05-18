# Last updated: 5/18/2026, 4:28:59 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxSum = 0
        minimum = prices[0]
        
        for i in range(1,len(prices)):

            if (prices[i] < minimum):
                minimum = prices[i]
            
            summ = prices[i] - minimum
            maxSum = max(summ,maxSum)
        
        return maxSum
                

        