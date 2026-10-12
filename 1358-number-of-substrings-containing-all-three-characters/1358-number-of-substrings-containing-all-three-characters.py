class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0 
        freq = {}
        length = 0
        max_len = 0
        count = 0
        n = len(s)
        while r<n:
            freq[s[r]] = freq.get(s[r],0) + 1
            print(freq)
            while len(freq)==3:
                freq[s[l]] = freq[s[l]] - 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l = l + 1
                count = count + n-r
            length = r-l+1
            r=r+1
        return count
