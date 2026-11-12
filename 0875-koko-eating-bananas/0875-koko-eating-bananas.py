class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            ssum=0
            for i in range(len(piles)):
                ssum = ssum + ceil(piles[i] / mid)
            if ssum<=h:
                high=mid-1
            else:
                low=mid+1
        return low


