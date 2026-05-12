# Last updated: 5/12/2026, 12:00:18 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for x in s:
            if ((x >= "a" and x <= "z") or (x>="0" and x<="9")):
                continue
            else:
                s=s.replace(x, "")
        j=-1

        for i in range(len(s)//2):
            if (s[i] != s[j]):
                return False
            j-=1
        return True
            