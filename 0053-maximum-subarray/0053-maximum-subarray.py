class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_ans=float('-inf')
        ans = 0
        for i in range(n):
            ans = ans + nums[i]
            max_ans = max(max_ans,ans)
            if ans<0:
                ans = 0
        return max_ans
