class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = []
        visited = [False]*n
        for i in range(n):
            graph.append([])
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        print(graph)

        def dfs(node):
            visited[node]=True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)


        count = 0
        for i in range(n):
            if visited[i]==False:
                count = count + 1 
                dfs(i)

        return count





