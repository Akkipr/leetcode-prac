# Last updated: 5/18/2026, 4:33:15 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit



        '''
        My attempt - same thing but using max()
        maxSum = 0
        minimum = prices[0]
        
        for i in range(1,len(prices)):

            if (prices[i] < minimum):
                minimum = prices[i]
            
            summ = prices[i] - minimum
            maxSum = max(summ,maxSum)
        
        return maxSum
                
        '''
        
                

        
