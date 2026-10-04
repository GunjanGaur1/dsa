class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        r = 0
        n = len(nums)
        count = 0
        ssum = 1
        while r<n:
            if k == 1:
                return 0
            ssum = ssum * nums[r]
            while ssum>=k:
                ssum = ssum/nums[l]
                l = l + 1
            count = count + (r-l+1)
            r = r + 1
        return count


