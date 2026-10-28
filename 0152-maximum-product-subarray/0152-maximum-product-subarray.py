class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = float('-inf')

        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1

            prefix = prefix*nums[i]
            suffix = suffix * nums[n-1-i]

            ans = max(ans, prefix, suffix)

        return ans
        