class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                high = mid-1
            elif nums[mid]<target:
                low = mid + 1
        
        lower_bound = low

        ## next part upper bound
        n = len(nums)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<=target:
                low = mid + 1
            elif nums[mid]>target:
                high = mid - 1
        
        higher_bound = high

        if lower_bound < n and nums[lower_bound]==target:
            return[lower_bound,higher_bound]

        return [-1,-1]

            

