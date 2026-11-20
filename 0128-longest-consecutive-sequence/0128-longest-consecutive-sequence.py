class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] = hash[nums[i]] + 1 
        longest=0 
        for current in hash:
            if current - 1 not in hash:
                count = 1     
                while current+1 in hash:
                    current=current+1
                    count=count+1
                longest=max(longest,count)
        return longest      