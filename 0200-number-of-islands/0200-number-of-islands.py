class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        visited = [[False] * cols for _ in range(rows)]
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0" or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited [i][j]:
                    count = count + 1
                    dfs(i, j)

        return count
        
        

