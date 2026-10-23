class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]<k:
                    ans = max(ans,nums[i]+nums[j])
        return ans
        