"""
Problem Link : https://leetcode.com/problems/fizz-buzz/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr = [0]*n
        for i in range(1, n+1):
            if (i%3 == 0 and i%5 == 0):
                arr[i-1] = "FizzBuzz"
            elif (i%3 == 0):
                arr[i-1] = "Fizz"
            elif (i%5 == 0):
                arr[i-1] = "Buzz"
            else:
                arr[i-1] = str(i)
        return arr


            
        
