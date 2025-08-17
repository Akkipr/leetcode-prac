# Last updated: 8/17/2025, 12:37:30 PM
class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [["IV", 4], ["IX", 9], ["XL", 40], ["CM" , 900], ["XC" , 90], ["CD", 400], ["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
        counter = 0
        i = 0
        while i<len(s):
            for j in range(len(count)):
                if (i<(len(s)-1) and count[j][0]==(s[i]+s[i+1])):
                    #print(key)
                    counter = counter+count[j][1]
                    i=i+2
                    break
                elif (i<(len(s)) and count[j][0]==(s[i])):
                    counter = counter+count[j][1] 
                    i=i+1
                    break
        return counter
        