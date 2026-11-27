
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = []
        visited = [0] * numCourses
        pathv = [0] * numCourses

        for i in range(numCourses):
            graph.append([])

        for u, v in prerequisites:
            graph[v].append(u)

        def isCycle(node):
            visited[node]=True
            pathv[node]=True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if isCycle(neighbor):
                        return True
                elif pathv[neighbor]==1:
                    return True
            pathv[node] = 0
            return False

        for i in range(numCourses):
            if not visited[i]:
                if isCycle(i):
                    return False

        return True
