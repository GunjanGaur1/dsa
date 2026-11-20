class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        m = len(board)
        n = len(board[0])
        count=0

        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return

            if board[i][j]=="X":
                board[i][j] = "."
            else:
                return

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="X":
                    count=count+1
                    dfs(i,j)

        return count

