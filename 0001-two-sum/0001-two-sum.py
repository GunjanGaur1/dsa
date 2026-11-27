class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        m=len(nums)
        hash = {}
        for i in range(n):
            if target - nums[i] in hash:
                return hash[target-nums[i]],i
            hash[nums[i]] = i 
            
        