class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            row = []
            for j in range(n):
                row.append(-1)
            dp.append(row)

        def solve(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0
        
            if dp[i][j] != -1:
                return dp[i][j]

        
            up = solve(i-1, j)
            left = solve(i, j-1)

            dp[i][j] = up + left
            return dp[i][j]

        return solve(m-1, n-1)