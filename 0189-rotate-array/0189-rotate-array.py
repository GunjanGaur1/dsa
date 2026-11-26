class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k = k % n
        left=0
        right=n-1
        def rev(left,right):
            while(left<right):
                nums[left],nums[right]=nums[right],nums[left]
                left=left+1
                right=right-1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)
        