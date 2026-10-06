class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        freq = {}
        max_len=0
        length =0

        while r<n:
            freq[s[r]] = freq.get(s[r], 0) + 1
            print(freq)
            for char,count in freq.items():
                max_freq = max(freq.values())
            window_length = r-l+1
            diff = window_length - max_freq
            while diff>k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l = l + 1
                window_length = r-l+1
                diff = window_length - max_freq
            length = r-l+1
            max_len = max(length,max_len)
            r=r+1
        return max_len
                
                
