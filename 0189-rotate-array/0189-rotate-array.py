class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k = k % n
        def rev(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left += 1
                right -= 1
        print(nums)
        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)
