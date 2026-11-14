class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        low = 0
        high = n-1
        first = -1
        last = -1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high = mid-1
            else:
                low=mid+1
        first = low

        ## last occurence 
        n=len(nums)
        low = 0
        high = n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        last = high

        if first<n and nums[first]==target:
            return[first,last]

        return [-1,-1]
