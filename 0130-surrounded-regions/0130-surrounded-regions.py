class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        row = len(board)
        col = len(board[0])
        count = 0

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return
            if board[i][j]=="X" or board[i][j]=="T" :
                return
            
            board[i][j]="T"

            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)

        for c in range(col):
            if(board[0][c]=="O"):
                dfs(0,c)
        for c in range(col):
            if(board[row-1][c]=="O"):
                dfs(row-1,c)
        for r in range(row):
            if(board[r][0]=="O"):
                dfs(r,0)
        for r in range(row):
            if(board[r][col-1]=="O"):
                dfs(r,col-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
        