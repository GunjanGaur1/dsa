class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        n = len(stones)
        for i in range(n):
            heapq.heappush(heap,-stones[i])
        while len(heap)>1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            x = first - second 
            heapq.heappush(heap,-x)
        return -heap[0] if heap else 0
