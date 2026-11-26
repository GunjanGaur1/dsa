class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))

        while queue:
            i, j, time = queue.popleft()
            directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]==1:
                    queue.append((ni,nj,time+1))
                    grid[ni][nj]=2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return time
