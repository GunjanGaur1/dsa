class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        k=0
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            if nums[i]%2==0:
                ans[k]=nums[i]
                k=k+2
        print(ans)
        k=1
        for i in range(n):
            if nums[i]%2!=0:
                ans[k]=nums[i]
                k=k+2
        return ans