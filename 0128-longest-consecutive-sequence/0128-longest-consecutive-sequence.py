class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1
        longest = 0
        for num in hash:
            current = num
            if current - 1 not in hash:
                count = 1

                while current+1 in hash:
                    current = current + 1
                    count = count + 1
                longest = max(longest,count)

        return longest
