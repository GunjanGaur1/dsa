class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count = count + 1
            else:
                count = 0
            if count>maxi:
                maxi = count
        return maxi
            
        

                

        