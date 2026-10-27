class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mini = 0
        n = len(nums)
        exp_sum = 0

        exp_sum = n*(n+1)//2

        sumi = sum(nums)

        return exp_sum-sumi


            