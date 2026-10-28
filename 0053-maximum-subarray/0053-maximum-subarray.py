class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        ssum = 0
        ans = float('-inf')
        for i in range(n):
            ssum = ssum + nums[i]
            print(ssum)
            ans = max(ans,ssum)
            print(ans)
            
            if ssum<0:
                ssum = 0
        return ans