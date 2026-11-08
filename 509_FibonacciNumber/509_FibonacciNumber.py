"""
Problem Link : https://leetcode.com/problems/fibonacci-number/
Platform     : LeetCode
Difficulty   : Easy
"""

class Solution:
    def fib(self, n: int) -> int:
        check = {0:0, 1:1}

        def fibbo(x):
            if x in check:
                return check[x]
            check[x] = fibbo(x-1) + fibbo(x-2)
            return check[x]
        
        return fibbo(n)
        
