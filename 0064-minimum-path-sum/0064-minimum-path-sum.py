class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp=[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(0)
            dp.append(row)
        print(dp)

        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j==0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]

                    dp[i][j] = grid[i][j] + min(up,left)
        
        return dp[n-1][m-1]
