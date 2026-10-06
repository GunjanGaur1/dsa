class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            if heights[i+1]>heights[i]:
                difference = heights[i+1]-heights[i]
                ##print(difference)
                heapq.heappush(heap,difference)
                ##print(heap)
                while len(heap)>ladders:
                    smallest = heapq.heappop(heap)
                    bricks = bricks - smallest
                    if bricks<0:
                        return i
        return len(heights)-1