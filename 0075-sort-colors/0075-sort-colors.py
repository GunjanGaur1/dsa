class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        low=0
        high=n-1
        mid=0
        low=mid


        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
            

        