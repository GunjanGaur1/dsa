class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        n = len(nums)
        # 2 5 7 8 10
        while low<=high:
            mid = (low+high)//2
            ssum = 0
            count = 1
            for i in range(n):
                if ssum+nums[i]>mid:
                    count = count+1
                    ssum = nums[i]
                else:
                    ssum = ssum + nums[i]

            if count<=k:
                high = mid - 1
            else:
                low = mid + 1

        return low

