class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        i = 0
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            ssum = 0
            for i in range(n):
                ssum = ssum + ceil(nums[i]/mid)
            if ssum<=threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low

