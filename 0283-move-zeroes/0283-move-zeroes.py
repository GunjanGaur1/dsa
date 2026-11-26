class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        ans = [0]*n
        j=0
        for i in range(n):
            if nums[i]!=0:
                ans[j]=nums[i]
                j=j+1

        nums[:] = ans

            
        