class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n=len(nums)
        low = 0
        high = n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid]==nums[high]:
                low=low+1
                high=high-1
            elif nums[low]<=nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low=mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low=mid+1
                else:
                    high = mid-1

        return False