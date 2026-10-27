class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = 0
        count1 = 0
        count2 = 0
        n = len(nums)
        result = []*n
        for i in range(n):
            if nums[i]==0:
                count=count+1
            elif nums[i]==1:
                count1=count1+1
            else:
                count2=count2+1
        for i in range(count):
            nums[i] = 0
        for i in range(count,count+count1):
            nums[i] = 1
        for i in range(count+count1,n):
            nums[i] = 2
        



        