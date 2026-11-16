class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n-1
        ans=[]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        first = low

        n = len(nums)
        low = 0
        high = n-1
        ans=[]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        last = high

        if first<n and nums[first]==target:
            return [first,last]
        else:
            return[-1,-1]
        
