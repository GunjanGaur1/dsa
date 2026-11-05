class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        max_len=0
        freq={}
        for i in range(n):
            for j in range(i+1,n+1):
                sub = s[i:j]
                freq[sub] = freq.get(sub, 0) + 1
                if freq[sub] >= 2:
                    max_len = max(max_len, len(sub))
        return max_len


