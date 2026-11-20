class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        visited = [False]*n
        graph = [[] for i in range(n)]


        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)

        def dfs(node):
            if node==destination:
                return True
            visited[node]=True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
            



            
