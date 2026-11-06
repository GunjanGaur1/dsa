class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        heap = []
        freq={}
        count=0
        result=[]
        prev = None
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            if prev:
                heapq.heappush(heap, prev)
            count = count+1
            if count<0:
                prev = (count,char)
            else:
                prev = None
        return "".join(result) if len(result) == len(s) else ""