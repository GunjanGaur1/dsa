class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        low = 1
        high = sum(sweetness)
        while low<=high:
            mid=(low+high)//2
            count=0
            ssum=0
            for i in range(len(sweetness)):
                #count=k+1
                ssum = ssum + sweetness[i]
                if ssum>=mid:
                    count=count+1
                    ssum=0
            if count>=k+1:
                low=mid+1
            else:
                high=mid-1
        return high

