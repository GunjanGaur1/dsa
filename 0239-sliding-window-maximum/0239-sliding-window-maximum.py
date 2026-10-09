class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0
        r = 0
        heap = []
        n = len(nums)
        ans = []

        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))

            while heap and heap[0][1]<i-k+1:
                heapq.heappop(heap)

            if i>=k-1:
                ans.append(-heap[0][0])
        return ans

