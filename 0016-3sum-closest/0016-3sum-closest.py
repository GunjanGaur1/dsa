class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        # -4 -1 1 2 
        ans=[]
        closest=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left = i+1
            right=n-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if abs(total-target)<abs(closest-target):
                    closest = total
                if total<target:
                    left=left+1
                else:
                    right=right-1
        return closest

                