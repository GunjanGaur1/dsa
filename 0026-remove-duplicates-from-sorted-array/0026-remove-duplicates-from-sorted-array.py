class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(1,n):
            if nums[k-1]==nums[i]:
                pass
            else:
                nums[k]=nums[i]
                k=k+1
        return k
