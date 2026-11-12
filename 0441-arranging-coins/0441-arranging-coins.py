class Solution:
    def arrangeCoins(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            ssum = mid * (mid+1)//2

            if ssum <=n:
                low=mid+1
            else:
                high=mid-1
        return high