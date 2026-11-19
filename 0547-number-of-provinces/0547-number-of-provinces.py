class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        count = 0
        

        def dfs(node):
            visited[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor]==1 and visited[neighbor]==0:
                    dfs(neighbor)
        for i in range(n):
            if not visited[i]:
                count=count+1
                dfs(i)



        return count

        