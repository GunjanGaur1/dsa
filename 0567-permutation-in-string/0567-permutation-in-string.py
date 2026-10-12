class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        l = 0 
        r=0
        freq = {}
        length = 0
        max_len = 0
        freq2 = {}
        for i in range(len(s1)):
            freq[s1[i]] = freq.get(s1[i],0) + 1
        print(freq)
        while r<n:
            if s2[r] in freq:
                freq2[s2[r]] = freq2.get(s2[r], 0) + 1
                window_length = r-l+1
                if window_length>len(s1):
                    freq2[s2[l]] -= 1
                    if freq2[s2[l]] == 0:
                        del freq2[s2[l]]
                    l += 1
                window_length = r-l+1
                if window_length == len(s1) and freq2==freq:
                    return True
                r=r+1

            else:
                freq2={}
                l = r + 1
                r=r+1

        return False




        