class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        ans = []
        i=0
       
        # -4,-1,-1,0,1,2

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while left<right and nums[left]==nums[left-1]:
                        left=left+1 
                    while left< right and nums[right]==nums[right+1]:
                        right=right-1

                elif nums[i]+nums[left]+nums[right]<0:
                    left=left+1
                else:
                    right=right-1
        return ans
