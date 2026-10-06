class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        count = 0
        max_len = 0
        length = 0
        for i in range(n):
            if nums[i]==0:
                count = count+1
                print("count",count)
                while count>k:
                    if nums[l]==0:
                        count = count-1
                    l = l + 1
            length = r-l+1
            max_len = max(max_len,length)
            r=r+1
        return max_len

