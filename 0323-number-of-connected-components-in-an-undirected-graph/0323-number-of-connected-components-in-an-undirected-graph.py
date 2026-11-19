class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[0] * n for i in range(n)]
        
        for u,v in edges:
            graph[u][v]=1
            graph[v][u]=1
        visited = [False]*n
        count = 0

        def dfs(node):
            visited[node]=True
            for neighbor in range(n):
                if graph[node][neighbor]==1 and not visited[neighbor]:
                    dfs(neighbor)
        for i in range(n):
            if not visited[i]:
                count=count+1
            dfs(i)
        return count





