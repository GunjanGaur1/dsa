class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]] = hash[nums[i]] + 1
                if hash[nums[i]] > 1:
                    return True
            else:
                hash[nums[i]] = 1
        
        return False
        