class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxarea=0

        def dfs(i,j):
            area = 1
            if i<0 or i>m-1 or j<0 or j>n-1:
                return 0

            if grid[i][j]==1:
                grid[i][j] = 0
            else:
                return 0

            area = area + dfs(i+1,j)
            area = area +dfs(i,j+1)
            area = area +dfs(i-1,j)
            area = area + dfs(i,j-1)

            return area
    
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area= dfs(i,j)
                    maxarea=max(maxarea,area)
                    print(maxarea)

        return maxarea

