# Last updated: 5/20/2026, 11:55:48 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_counts = {}
        longest_substring = 0

        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
        
            max_freq = max(max_freq, char_counts[s[right]])
            
            while (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
                
            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring