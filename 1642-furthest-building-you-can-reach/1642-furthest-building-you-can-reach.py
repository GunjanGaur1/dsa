class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n-1):
            if heights[i+1]>heights[i]:
                difference = heights[i+1]-heights[i]
                heapq.heappush(heap,difference)
                ##print(heap)
                while len(heap)>ladders:
                    x = heapq.heappop(heap)
                    bricks = bricks - x
            if(bricks<0):
                return i
        return n-1

        