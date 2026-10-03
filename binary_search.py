class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low<=high:
            mid = (low+high)//2
            ssum = 0
            count = 1
            for i in range(len(nums)):
                if ssum + nums[i]>mid:
                    count = count + 1
                    ssum = nums[i]
                else:
                    ssum = ssum + nums[i]
            if count > k:
                low = mid + 1
            else:
                high = mid - 1 

        return low
