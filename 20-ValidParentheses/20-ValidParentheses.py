# Last updated: 12/29/2025, 11:57:07 PM
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in matching.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != matching[char]:
                    return False

        return not stack
 


            
            

        