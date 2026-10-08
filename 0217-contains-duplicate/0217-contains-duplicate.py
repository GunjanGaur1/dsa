class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                return True
        return False
        