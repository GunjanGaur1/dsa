class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low+high)//2
            ssum = 0
            count = 1
            for i in range(len(weights)):
                ssum = ssum + weights[i]
                if ssum>mid:
                    count = count + 1
                    ssum = weights[i]
            if count<=days:
                high=mid-1
            else:
                low=mid+1
        return low