class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if n==1:
                return nums[0]
            if mid==0:
                if nums[mid]!=nums[mid+1]:
                    return nums[mid]
                else:
                    low=mid+1
            elif mid==n-1:
                if nums[mid]!=nums[mid-1]:
                    return nums[mid]
                else:
                    high=mid-1
            elif nums[mid]==nums[mid+1]:
                if mid%2==0:
                    low=mid+2
                else:
                    high=mid-1
            elif nums[mid]==nums[mid-1]:
                if mid%2==0:
                    high=mid-1
                else:
                    low=mid+1
            else:
                return nums[mid]
