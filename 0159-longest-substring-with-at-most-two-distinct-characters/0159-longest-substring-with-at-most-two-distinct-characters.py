class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        freq = {}
        max_len = 0
        length = 0

        while r<n:
            freq[s[r]] = freq.get(s[r],0) + 1
            while len(freq)>2:
                freq[s[l]] = freq[s[l]] - 1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l = l + 1
            length = r-l+1
            max_len = max(max_len,length)
            r=r+1

        return max_len