class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count=0
        visited=[False]*n

        def dfs(node):
            visited[node]=True
            for neighbor in range(n):
                if not visited[neighbor] and isConnected[node][neighbor]==1:
                    dfs(neighbor)
        for i in range(n):
            if not visited[i]:
                count=count+1
                dfs(i)

        return count