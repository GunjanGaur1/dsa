class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0 
        r = 0
        n = len(nums)
        result = []
        heap = []

        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))
            if i==k-1:
                maxi= heap[0][0]
                result.append(-maxi)
            elif i>k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                maxi = heap[0][0]
                result.append(-maxi)
        return result
