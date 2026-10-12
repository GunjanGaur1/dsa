class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        n = len(nums)
        while low<=high:
            mid = (low+high)//2
            ssum = 0
            for i in range(n):
                ssum = ssum + ceil(nums[i]/mid)
            if ssum>threshold:
                low = mid+1
            else:
                high = mid-1
        return low
        