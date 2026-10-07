class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        shapes = set()
        ##island = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c]!=1:
                return
            grid[r][c]=0

            shape.append("R")
            dfs(r, c + 1)
            shape.append("B")
            shape.append("U")
            dfs(r - 1, c)
            shape.append("B")
            shape.append("L")
            dfs(r, c - 1)
            shape.append("B")
            shape.append("D")
            dfs(r + 1, c)
            shape.append("B")


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    ##island = island + 1
                    shape = []
                    dfs(i,j)
                    shapes.add(tuple(shape))
        return len(shapes)