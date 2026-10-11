class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        ans = []
        mini = 0
        
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            #print(heap)
            if i==k-1:
                mini = -heap[0][0]
                ans.append(mini)
            elif i>=k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                mini = -heap[0][0]
                ans.append(mini)
        return ans
