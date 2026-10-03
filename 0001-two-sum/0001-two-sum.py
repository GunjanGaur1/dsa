class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i] + nums[j]) == target:
                    return [i,j]