class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        m=len(nums)
        for i in range(n):
            for j in range(i+1,m):
                if nums[i]+nums[j]==target:
                    return i,j
        