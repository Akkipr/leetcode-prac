# Last updated: 8/18/2025, 1:17:43 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        master_count=0
        counter=0
        seen_chars = []
        if (len(s)==1):
            return 1
        for j in range(len(s)):
            seen_chars.append(s[j])
            counter+=1
            for i in range(j+1, len(s)):
                if (s[i] in seen_chars):
                    if (counter>master_count):
                        master_count=counter
                    counter=0
                    seen_chars = []
                    break
                else:
                    seen_chars.append(s[i])
                    counter=counter+1
            if (counter>master_count):
                master_count=counter
            counter=0
        return master_count
        