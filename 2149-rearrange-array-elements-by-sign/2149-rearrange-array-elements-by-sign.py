class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans = [0]*n
        k = 0
        pos = 0 
        neg = 1
        for i in range(n):
            if nums[i]>0:
                ans[pos]=nums[i]
                pos = pos + 2
            elif nums[i]<0:
                ans[neg] = nums[i]
                neg = neg + 2
        return ans
            
