class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        max_len = 0
        length = 0
        count = 0
        #  nums = [1,1,1,0,0,0,1,1,1,1,0]

        while r<n:
            if nums[r]==0:
                count = count + 1
                while count>k:
                    if nums[l]==0:
                        count = count - 1
                    l = l + 1
            length = r-l+1
            max_len = max(length,max_len)
            r=r+1

        return max_len

            