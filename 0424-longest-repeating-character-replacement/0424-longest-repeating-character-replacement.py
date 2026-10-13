class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        max_freq = 0
        length = 0
        max_length = 0
        freq={}
        while r<n:
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(max_freq,freq[s[r]])
            window_length = r-l+1
            replacement = window_length - max_freq
            if replacement>k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
                if freq[s[l]] ==0:
                    del freq[s[l]]
            length = r-l+1
            print(length)
            max_length = max(max_length,length)
            print(max_length)
            r=r+1
        
        return max_length
