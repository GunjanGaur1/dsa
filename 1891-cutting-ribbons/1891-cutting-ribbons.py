class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        low = 1
        high = max(ribbons)
        ans=0
        while low<=high:
            mid=(low+high)//2
            ## low = 1, high=9 mid = 5
            count = 0
            for i in range(len(ribbons)):
                count = count + ribbons[i] // mid
            if count<k:
                high=mid-1
            else:
                ans = mid
                low=mid+1
        return ans
                