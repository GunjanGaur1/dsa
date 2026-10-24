class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]] = hash[nums[i]] + 1
            else:
                hash[nums[i]] = 1
        print(hash)

        sorted_nums = sorted(hash,key=hash.get,reverse = True)

        return sorted_nums[:k]