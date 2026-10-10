class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        freq = {}
        max_freq = 0
        max_len = 0
        while r<n:
            freq[s[r]]=freq.get(s[r],0) + 1
            max_freq = max(max_freq,freq[s[r]])
            print(freq)
            window_length = r-l+1
            difference = window_length - max_freq
            if difference>k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
            length = r-l+1
            max_len = max(length,max_len)
            r = r+1

        return max_len
