class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands=0

        def dfs(i,j):
            if i<0 or j<0 or i>n-1 or j>m-1:
                return
            if grid[i][j] != "1":
                return
    
            grid[i][j]="0"

            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    islands=islands+1
                    dfs(i,j)
        return islands