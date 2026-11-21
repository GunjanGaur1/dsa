class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        hash={0:-1}
        count=0
        prefix=0
        maxlen=0
        for i in range(len(nums)):
            prefix=prefix+nums[i]
            if prefix-k in hash:
                length = i - hash[prefix-k]
                if length>maxlen:
                    maxlen=length
            if prefix not in hash:
                hash[prefix] = i
        return maxlen

