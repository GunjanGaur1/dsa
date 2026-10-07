class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        t = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j,0)) 
        while queue:
            r,c,t = queue.popleft()

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc,t+1)) 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return t