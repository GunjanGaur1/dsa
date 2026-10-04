class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        n = len(nums)
       
        while low<=high:
            mid = (low+high)//2
            ssum = 0
            count = 1 # this is a subarray we have whatever fits is <=mid

            for i in range(n):
                if ssum + nums[i]<= mid:
                    ssum = ssum + nums[i]
                else:
                    count = count + 1
                    ssum = nums[i]
            if count<=k:
                high = mid-1
            else:
                low = mid+1

        return low


           