class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        low = 0
        high = max(start) + d - min(start)

        while low <= high:
            mid = (low + high) // 2

            chosen = start[0]
            possible = True

            for i in range(1, len(start)):
                new = max(chosen + mid, start[i])

                if new > start[i] + d:
                    possible = False
                    break

                chosen = new

            if possible:
                low = mid + 1
            else:
                high = mid - 1

        return high