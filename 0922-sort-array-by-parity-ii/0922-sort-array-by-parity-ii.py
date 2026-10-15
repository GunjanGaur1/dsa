class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0]*n
        even = 0
        odd = 1
        for i in range(n):
            if nums[i]%2==0:
                res[even] = nums[i]
                even = even + 2
            else:
                res[odd] = nums[i]
                odd = odd + 2
        return res