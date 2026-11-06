class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        perimeter = 0

        def dfs(r,c):
            nonlocal perimeter
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                perimeter += 1
                return
            if (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    return perimeter
        return perimeter

