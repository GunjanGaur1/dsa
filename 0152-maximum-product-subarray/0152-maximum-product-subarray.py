class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix = 1
        suffix = 1
        ssum = float('-inf')
        n = len(nums)
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-1-i]
            ssum = max(ssum,prefix,suffix)
        return ssum