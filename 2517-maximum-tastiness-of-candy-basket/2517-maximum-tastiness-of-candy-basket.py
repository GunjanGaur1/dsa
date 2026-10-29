class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        price.sort()
        low = 0
        high = price[-1]-price[0]
        n = len(price)
        # 1 2 5 8 13 21 
        
        while low<=high:
            mid=(low+high)//2
            prev=price[0]
            count = 1
            for i in range(n):
                if price[i]-prev>=mid:
                    count=count+1
                    prev=price[i]
            if count>=k:
                ans=mid
                low = mid+1
            else:
                high=mid-1
        return ans