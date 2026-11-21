class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix=0
        hash={0:-1}
        count=0
        max_length=0
        for i in range(len(nums)):
            prefix=prefix+nums[i]
            target = prefix - k
            if target in hash:
                length = i - hash[target]
                if length > max_length:
                    max_length = length
            if prefix not in hash:
                hash[prefix] = i
        return max_length


        
