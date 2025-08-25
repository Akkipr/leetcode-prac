# Last updated: 8/25/2025, 1:54:49 AM
import math
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_array = []
        array = []  
        stuff = strs

        for i in range(len(strs)):
            main_track = 0
            for j in range(i+1, len(strs)):
                if (len(strs[i]) == len(strs[j]) and strs[i] != "garbageval" and strs[j] != "garbageval"):
                    p = 0
                    count = 0
                    fail = 0
                    x = strs[i]
                    y = strs[j]
                    try:
                        while (p <= len(x) and (len(x)==len(y))):
                            if (x[count] in y):
                                letter_to_replace=x[count]
                                l = x.count(x[count])
                                x = x.replace(letter_to_replace, "")
                                y = y.replace(letter_to_replace, "")
                                p = p-l
                            else:
                                fail = 1
                                break
                            p +=1
                    except Exception:
                        pass
                    if ((len(x) != len(y)) ):
                        fail = 1
                    if fail==0:
                        main_track = 1
                        if (strs[i] not in array):
                            array.append(strs[i])
                        array.append(strs[j])
                        strs[j] = "garbageval"
            if (len(array)>0):
                main_array.append(array)
            array = []
            if main_track == 1:
                strs[i] = "garbageval"
            elif main_track==0 and strs[i]!="garbageval":
                main_array.append([strs[i]])
        return main_array


                        

