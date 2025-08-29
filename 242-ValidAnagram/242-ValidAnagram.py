# Last updated: 8/28/2025, 9:20:19 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 2
        dict_t = {}
        dict_s = {}

        if len(s) == len(t):
            for i in range(len(s)):
                if (s[i] in dict_s):
                    dict_s[s[i]] = dict_s[s[i]] + 1
                if (t[i] in dict_t):
                    dict_t[t[i]] = dict_t[t[i]] + 1
                if (t[i] not in dict_t):
                    dict_t[t[i]] = 1
                if (s[i] not in dict_s):
                    dict_s[s[i]] = 1
            return dict_s == dict_t
        else:
            return False



        '''
        # Solution 1
        s = sorted(s)
        s = "".join(s)
        t = sorted(t)
        t = "".join(t)

        return s==t


        if (s[i] not in dict_s or t[i] not in dict_t):
                    if (t[i] not in dict_t):
                        dict_t[t[i]] = 1
                    if (s[i] not in dict_s):
                        dict_s[s[i]] = 1
                    continue
                else:
                    if (s[i] in dict_s):
                        dict_s[s[i]] = dict_s[s[i]] + 1
                    if (t[i] in dict_t):
                        dict_t[t[i]] = dict_t[t[i]] + 1
        '''

        

        
