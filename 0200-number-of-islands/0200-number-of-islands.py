class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        print(rows)
        cols = len(grid[0])
        print(cols)
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if grid[r][c] == "0":
                return
            grid[r][c]="0"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    islands = islands + 1
                    dfs(i,j)
        return islands
