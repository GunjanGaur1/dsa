class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash:
                if i - hash[nums[i]]<=k:
                    return True
            hash[nums[i]] = i
        return False
