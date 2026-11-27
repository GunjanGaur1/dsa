class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[]
        for i in range(m):
            row = []
            for j in range(n):
                row.append(-1)
            dp.append(row)

        def solve(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]
            
            left = solve(i-1,j)
            right = solve(i,j-1)
            dp[i][j] = left+right
            return dp[i][j]

        return solve(m-1,n-1)