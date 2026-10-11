class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        heap = []
        fuel = startFuel # starts at 10
        stops = 0 
        n = len(stations)
        stations = stations + [[target, 0]]
        positions = 0

        for position,capacity in stations:
            fuel = fuel - (position - positions)
            positions = position
            while fuel<0:
                if not heap:
                    return -1 
                fuel += -heapq.heappop(heap)
                stops = stops + 1
            heapq.heappush(heap,-capacity)

        return stops




        
        