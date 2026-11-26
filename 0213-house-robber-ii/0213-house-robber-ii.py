class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        #n=3
        dp=[0]*(n-1)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        dp[0]=nums[1]
        dp[1]=max(nums[1],nums[2])
        for i in range(2,n-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i+1])
        
        first = dp[n-2]

        n=len(nums)
        #n=3
        dp=[0]*(n-1)

        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        
        last = dp[n-2]

        return max(first,last)
        
        