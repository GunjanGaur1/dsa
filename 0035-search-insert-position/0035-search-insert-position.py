class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        #n=6 elements 
        low = 0
        high = n-1
        #high=
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high = mid -1
        return low