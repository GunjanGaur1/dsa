class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = set(nums)
        longest = 0
        for num in hash:
            if num - 1 not in hash:
                count = 1
                current = num
                while current + 1 in hash:
                    current = current + 1
                    count = count + 1
                
                longest = max(longest, count)
        return longest
            
