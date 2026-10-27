class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement], i]
            hash[nums[i]] = i