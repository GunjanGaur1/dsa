class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in hash:
                return hash[target-nums[i]],i
            else:
                hash[nums[i]] = i
