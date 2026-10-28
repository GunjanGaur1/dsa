class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans=[]
        count=0 
        for i in range(n-2):
            left = i+1
            right=n-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total<target:
                    count=count+right-left
                    left=left+1
                else:
                    right=right-1

        return count