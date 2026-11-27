class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {}
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch]=[]
        print(adj)

        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            if len(s1) > len(s2) and s1.startswith(s2):
                return ""

            for j in range(min(len(s1), len(s2))):
                if s1[j] != s2[j]:
                    adj[s1[j]].append(s2[j])
                    break
        print(adj)
        indegree = {}
        for ch in adj:
            indegree[ch] = 0

        for ch in adj:
            for neighbor in adj[ch]:
                indegree[neighbor] += 1

        from collections import deque
        queue = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
        topo=[]
        while queue:
            node = queue.popleft()
            topo += node
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo) != len(adj):
            return ""

        return "".join(topo)


        