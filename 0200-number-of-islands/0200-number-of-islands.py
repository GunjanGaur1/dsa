class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[False] * cols for i in range(rows)]

        def dfs(r,c):
            if r<0 or r>=rows or c>=cols or c<0:
                return
            ## boundary condition
            if visited[r][c]:
                return
            
            if grid[r][c]=="0":
                return
            ## check if its 0 we return 
            visited[r][c]=True


            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r+1,c)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and not visited[i][j]:
                    ##count as soon as u get a 1 
                    count = count + 1
                    dfs(i,j)

        return count 