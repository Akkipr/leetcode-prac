# Last updated: 5/12/2026, 12:16:00 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


        '''
        My attempt - works but runtime is bad
        s=s.lower()
        for x in s:
            if (x.isalnum()):
                continue
            else:
                s=s.replace(x, "")
        j=-1

        for i in range(len(s)//2):
            if (s[i] != s[j]):
                return False
            j-=1
        return True
        '''
            
            
