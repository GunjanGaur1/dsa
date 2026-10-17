class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        n = len(nums)
        hash = {}
        for i in range(n):
            if nums[i]%2==0:
                if nums[i] in hash:
                    hash[nums[i]] = hash[nums[i]] + 1
                else:
                    hash[nums[i]] = 1
        if not hash:
            return -1

        return min(hash, key=lambda x: (-hash[x], x))
            