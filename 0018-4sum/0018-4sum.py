class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    total = nums[i]+nums[left]+nums[right]+nums[j]
                    if total == target:
                        triplet = [nums[i],nums[j],nums[left],nums[right]]
                        ans.append(triplet)
                        left=left+1
                        right=right-1
                        while left<right and nums[left]==nums[left-1]:
                            left=left+1
                        while left<right and nums[right]==nums[right+1]:
                            right=right-1
                    elif total<target:
                        left=left+1
                    else:
                        right=right-1
        return ans
                