class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        k=1
        for i in range(1,n):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k=k+1
        return k
                

