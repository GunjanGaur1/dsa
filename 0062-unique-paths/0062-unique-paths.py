class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(0)
            dp.append(row)
        
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0:
                    dp[i][j] = 1
                else:
                    left = dp[i-1][j]
                    right = dp[i][j-1]
                    dp[i][j]=left+right
                    
        return dp[m-1][n-1]
