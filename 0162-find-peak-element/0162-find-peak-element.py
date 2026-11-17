class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if n==1:
                return 0
            if mid==0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low=mid+1
            elif mid==n-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    high=mid
            else: 
                if nums[mid]<nums[mid+1]:
                    low=mid+1
                else:
                    high=mid
        return low
        
