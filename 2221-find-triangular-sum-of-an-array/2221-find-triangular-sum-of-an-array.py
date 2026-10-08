class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            result = []

            for i in range(len(nums) - 1):
                result.append((nums[i] + nums[i + 1]) % 10)

            nums = result
            #print(result)

        return nums[0]