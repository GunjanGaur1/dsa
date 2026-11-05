class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        r=0
        n=len(nums)
        max_len=float('inf')
        length =0
        ssum=0
        while r<n:
            ssum = ssum + nums[r]
            while ssum>=target:
                length = r-l+1
                max_len = min(max_len,length)
                
                ssum=ssum-nums[l]
                l=l+1
            r=r+1
        return 0 if max_len == float('inf')  else max_len