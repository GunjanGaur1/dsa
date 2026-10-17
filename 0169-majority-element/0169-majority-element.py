class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        hash = {}

        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]] = hash[nums[i]] + 1
            else:
                hash[nums[i]] = 1
        
        return max(hash, key=hash.get)