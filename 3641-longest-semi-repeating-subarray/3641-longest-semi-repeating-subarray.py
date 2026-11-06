class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash = {}
        l=0
        r=0
        freq={}
        repeating = 0
        max_len=0
        while r<n:
            if nums[r] not in hash:
                hash[nums[r]] = 1
            else:
                hash[nums[r]] += 1   
            if hash[nums[r]] == 2:
                repeating += 1    
                while repeating>k:
                    hash[nums[l]] = hash[nums[l]] - 1
                    if hash[nums[l]] == 1:
                        repeating -= 1
                    l=l+1
            max_len=max(max_len,r-l+1)
            r=r+1
        return max_len
