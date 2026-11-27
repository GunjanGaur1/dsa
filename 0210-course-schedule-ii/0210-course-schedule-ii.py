class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegree=[0]*numCourses

        adj = []
        for i in range(numCourses):
            adj.append([])
        for i,j in prerequisites:
            adj[j].append(i)
        print(adj)

        indegree = [0] * numCourses

        for i, j in prerequisites:
            indegree[i]+=1
        print(indegree)

        queue = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node = queue.popleft()
            topo.append(node)

            for neighbor in adj[node]:
                indegree[neighbor]=indegree[neighbor]-1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo)==numCourses:
            return topo

        return []
