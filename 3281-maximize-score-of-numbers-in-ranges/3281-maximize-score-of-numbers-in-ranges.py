class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        low = 0
        high = max(start) + d - min(start)
        start.sort()

        while low<=high:
            mid = (low+high)//2
            possible = True
            chosen = start[0]
            for i in range(1,len(start)):
                new = max(chosen + mid, start[i])
                if new<=start[i]+d:
                    chosen = new
                else:
                    possible = False
                    break
            if possible:
                low = mid+1
            else:
                high = mid-1
        return high


