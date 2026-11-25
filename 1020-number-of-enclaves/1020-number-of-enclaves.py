class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return
            if grid[i][j]==0:
                return
            
            grid[i][j]=0

            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)

        for c in range(col):
            if(grid[0][c]==1):
                dfs(0,c)
        for c in range(col):
            if(grid[row-1][c]==1):
                dfs(row-1,c)
        for r in range(row):
            if(grid[r][0]==1):
                dfs(r,0)
        for r in range(row):
            if(grid[r][col-1]==1):
                dfs(r,col-1)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count=count+1

        return count