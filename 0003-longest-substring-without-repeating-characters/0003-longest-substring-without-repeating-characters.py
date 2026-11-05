class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        freq = {}
        l=0
        max_len = 0
        count=0
        for r in range(n):
            freq[s[r]] = freq.get(s[r],0) + 1
            count=count+1
            while freq[s[r]]>1:
                freq[s[l]] -= 1
                l=l+1
                count=count-1
            max_len = max(max_len,count)
        return max_len

