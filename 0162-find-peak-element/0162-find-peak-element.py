class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        for i in range(n):
            if i==0:
                if nums[i]>nums[i+1]:
                    return i 
            elif i==n-1:
                if nums[i]>nums[i-1]:
                    return i
            else:
                if nums[i-1]<nums[i]>nums[i+1]:
                    return i
