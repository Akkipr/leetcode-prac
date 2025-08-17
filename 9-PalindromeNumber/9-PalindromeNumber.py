# Last updated: 8/17/2025, 12:37:29 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c = str(x)
        x = len(c)
        y = x-1
        z=0
        if (x%2==0):
            q = x/2
            for i in range(q):
                if c[i]!=c[y-i]:
                    return False
        else:
            q = y/2
            for i in range(q):
                if c[i]!=c[y-i]:
                    return False
        return True
        

        