class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        prev = 0
        curr = 1
        ans = 0
        for i in range(n-1):
            if s[i]==s[i+1]:
                curr = curr+1
            else:
                ans = ans + min(prev,curr)
                prev = curr 
                curr=1
        return ans + min(prev,curr)