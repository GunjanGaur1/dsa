class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0
        r = 0
        n = len(nums)
        heap = []
        result = []
        mini = 0

        for i in range(n):
            heapq.heappush(heap,(-nums[i],i))
            if i==k-1:
                mini = -heap[0][0]
                result.append(mini)
                print(heap)
                print(result)
            elif i>=k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                mini = -heap[0][0]
                ##print("mini",mini)
                result.append(mini)
                ##print(result)
        return result



