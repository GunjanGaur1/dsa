class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 0
        seen = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in seen:
                return seen[complement],i

            seen[nums[i]] = i
        
