class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        n = len(nums)
        for i in range(n):
            compliment = target - nums[i]
            if compliment in hash:
                return hash[compliment],i
            hash[nums[i]] = i
