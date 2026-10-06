class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        n = len(s)
        freq = {}
        for i in range(n):
            freq[s[i]] =  freq.get(s[i],0) + 1
        
        for char,count in freq.items():
            heapq.heappush(heap,(-count,char))
            print(heap)

        prev_freq = 0
        prev_char = ''
        result =  []

        while heap:
            freq,char = heapq.heappop(heap)
            print(heap)
            if prev_freq<0:
                heapq.heappush(heap,(prev_freq,prev_char))
                print("prev",heap)
            result.append(char)
            print("result",result)
            freq = freq + 1 
            prev_freq = freq
            prev_char = char

        if prev_freq:
            return ""
        
        return "".join(result)






        
        