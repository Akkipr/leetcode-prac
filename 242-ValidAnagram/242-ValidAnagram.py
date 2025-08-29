# Last updated: 8/28/2025, 8:46:39 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        s = "".join(s)
        t = sorted(t)
        t = "".join(t)

        return True if s==t else False

        