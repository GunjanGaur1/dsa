class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        even = 0
        odd = 1
        ans = [0]*n

        for i in range(n):
            if nums[i]%2==0:
                ans[even]=nums[i]
                even = even + 2
            else:
                ans[odd]=nums[i]
                odd=odd+2
        return ans