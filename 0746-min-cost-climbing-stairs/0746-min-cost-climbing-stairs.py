class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp = [0]*(n+1)
        # 0 0 0 0 
        # 10 15 , 15
        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i]=min(dp[i-2]+cost[i],dp[i-1]+cost[i])


        return min(dp[n-1],dp[n-2])

