class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        n = len(stones)

        for i in range(n):
            heapq.heappush(heap,-stones[i])
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            diff = x-y
            heapq.heappush(heap,-diff)
        return -heap[0] if heap else 0
