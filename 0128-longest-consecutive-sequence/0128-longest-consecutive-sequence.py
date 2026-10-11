class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] = hash[nums[i]] + 1
        print(hash)

        max_count = 0
        for num in hash:
            if num-1 not in hash:
                count = 1
                current = num
                while current+1 in hash:
                    count = count + 1
                    current = current + 1
                max_count = max(max_count,count)
        return max_count