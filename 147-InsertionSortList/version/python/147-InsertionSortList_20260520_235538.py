# Last updated: 5/20/2026, 11:55:38 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left = 0
4        max_freq = 0
5        char_counts = {}
6        longest_substring = 0
7
8        for right in range(len(s)):
9            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
10        
11            max_freq = max(max_freq, char_counts[s[right]])
12            
13            while (right - left + 1) - max_freq > k:
14                char_counts[s[left]] -= 1
15                left += 1
16                
17            longest_substring = max(longest_substring, right - left + 1)
18
19        return longest_substring