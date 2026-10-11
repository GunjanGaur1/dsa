class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        min_len = 0
        length = 0
        count = 0
        while r<n:
            if nums[r]==0:
                count = count + 1
                while count>k:
                    if nums[l]==0:
                        count = count - 1
                    l = l + 1
            length = r-l+1
            min_len = max(min_len,length)
            r=r+1
        return min_len