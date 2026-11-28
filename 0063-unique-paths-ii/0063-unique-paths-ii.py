class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = []
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(0)
            dp.append(row)
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i==0 and j ==0:
                    dp[i][j] = 1
                else:
                    left = dp[i-1][j] if i>0 else 0
                    right = dp[i][j-1] if j>0 else 0
                    dp[i][j]=left+right
                    
        return dp[n-1][m-1]
