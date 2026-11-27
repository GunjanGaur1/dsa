class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        rev = []
        from collections import deque
        queue = deque()
        for i in range(n):
            rev.append([])
        

        for i in range(n):
            for neighbor in graph[i]:
                rev[neighbor].append(i)

        outdegree=[0]*n

        for i in range(n):
            outdegree[i] = len(graph[i])

        for i in range(n):
            if outdegree[i]==0:
                queue.append(i)
        
        topo = []
        
        while queue:
            node = queue.popleft()
            topo.append(node)

            for neighbor in rev[node]:
                outdegree[neighbor]-=1
                if outdegree[neighbor]==0:
                    queue.append(neighbor)
        return sorted(topo)

        

        
        
