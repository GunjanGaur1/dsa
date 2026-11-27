class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        ssum = 0
        maxi=float('-inf')
        
        for i in range(n):
            ssum = ssum + nums[i]
            maxi=max(ssum,maxi)
            if ssum<0:
                ssum = 0
        return maxi
        
                