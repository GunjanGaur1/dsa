class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[None] * n for _ in range(n)]
        def solve(i, j):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] is not None:
                return dp[i][j]

            down = solve(i+1,j)
            diag = solve(i+1,j+1)

            dp[i][j] = triangle[i][j] + min(down, diag)
            
            return dp[i][j]

        return solve(0,0)
        


        