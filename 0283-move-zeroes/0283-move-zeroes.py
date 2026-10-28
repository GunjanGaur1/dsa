class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        k = 0
        ans = [0]*n
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k=k+1
        while k<n:
            nums[k]=0
            k=k+1

