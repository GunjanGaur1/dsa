class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        ans = []
        
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            print(heap)
            if i==k-1:
                ans.append(-heap[0][0])
            elif i>=k-1:
                if heap[0][1]>i-k:
                    ans.append(-heap[0][0])
        return ans





