class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        n = len(nums)
        ans = [0]*n
        for i in range(len(nums)):
            if nums[i]!=0:
                ans[k]=nums[i]
                k=k+1
        nums[:] = ans

        