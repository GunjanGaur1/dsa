class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        n = len(nums)
        ans = []
        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))
            ##print(heap)
            if i == k-1:
                x= -heap[0][0]
                ans.append(x)
                ##print(ans)
            elif i>k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                ##print("after pop",heap)
                x=-heap[0][0]
                ##print("2nd",x)
                ans.append(x)
                    
        return ans
