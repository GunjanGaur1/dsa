class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        low=0
        high=n-1

        while low<high:
            mid=(low+high)//2
            if arr[mid]>=arr[mid+1]:
                high=mid
            else:
                low=mid+1
        return low

            

