class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        maxcount=0

        for i in range(n):
            if nums[i]==1:
                count = count + 1
                maxcount = max(count,maxcount)
            elif nums[i]==0:
                count = 0

        return maxcount