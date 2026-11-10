class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low = 0
        high = n-1
        ans=-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                return mid
        return -1
