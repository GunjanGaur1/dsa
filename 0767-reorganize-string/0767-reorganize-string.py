class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = {}
        n = len(s)
        ans = []
        result = []
        for i in range(n):
            freq[s[i]] = freq.get(s[i],0) + 1
        for char,count in freq.items():
            heapq.heappush(heap, (-count, char))
        prev_freq = 0
        prev_char = ""
        while heap:
            freq,char = heapq.heappop(heap)
            freq = freq+1
            result.append(char)

            if prev_freq<0:
                heapq.heappush(heap,(prev_freq,prev_char))
            
            prev_freq= freq
            prev_char = char
        if prev_freq:
            return ""

        return "".join(result)
            

