# Last updated: 8/18/2025, 4:08:21 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word_append = ""
        length = 0
        index = 0
        invalid = 0

        for i in range(len(strs)):
            if (len(strs[i]) > length):
                length = len(strs[i])
                index = i

        for j in range(length):
            try:
                for h in range(len(strs)):
                    if (strs[h][j] != strs[i][j]):
                        invalid=1
                if (invalid!=1):
                    word_append = word_append + strs[i][j]
                else:
                    return word_append
            except Exception:
                return word_append
        return word_append
