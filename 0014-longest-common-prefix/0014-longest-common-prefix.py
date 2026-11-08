class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs[0])
        prefix = ""
        for i in range(n):
            for j in range(len(strs)):
                if i>=len(strs[j]):
                    return prefix
                if strs[j][i]!=strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix