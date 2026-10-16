class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] = hash[nums[i]] + 1
        return max(hash, key=hash.get)