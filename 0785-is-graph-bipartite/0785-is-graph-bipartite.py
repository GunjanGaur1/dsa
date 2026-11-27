class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False]*n
        color = [-1]*n

        def dfs(node,col):
            visited[node]=True
            color[node]=col

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor,1-col):
                        return False
                elif color[neighbor]==col:
                    return False
            return True

        for i in range(n):
            if not visited[i]:
                if not(dfs(i,0)):
                    return False
        return True