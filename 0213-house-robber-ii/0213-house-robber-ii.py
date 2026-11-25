class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp=[0]*(n)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        dp[0]=nums[1]
        dp[1]=max(nums[1],nums[2])
        for i in range(2,n-1):
            dp[i]= max(nums[i+1]+dp[i-2],dp[i-1])
        first =  dp[n-2]

        ## excluding the last
        n = len(nums)
        dp=[0]*(n)
        if n==1:
            return nums[0]

        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            dp[i]= max(nums[i]+dp[i-2],dp[i-1])
        last =  dp[n-2]

        return(max(first,last))