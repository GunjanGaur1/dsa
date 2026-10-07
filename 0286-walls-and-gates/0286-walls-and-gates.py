class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        rows = len(rooms)
        cols = len(rooms[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j]==0:
                    queue.append((i,j,0))

        while queue:
            r,c,distance = queue.popleft(
            )
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==2147483647:
                    rooms[nr][nc]= distance + 1
                    queue.append((nr,nc,distance+1))
        

        