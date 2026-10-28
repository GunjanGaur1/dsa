class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        ssum = float('-inf')
        curr = nums[0]
        ans=0
        for i in range(n):
           ans = ans + nums[i]
           ssum = max(ssum,ans)
           #print("ans",ans)
           if ans<0:
            ans=0
        return ssum
