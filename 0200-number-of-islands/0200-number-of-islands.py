class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n=len(grid[0])

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j]="0"

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count=count+1
                    dfs(i,j)

        return count