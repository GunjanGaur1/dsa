class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        n = len(nums)
        even = []
        odd = []

        for i in range(n):
            if i%2!=0:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        
        even.sort()
        odd.sort(reverse=True)

        ans = [0] * n

        ans[::2] = even
        ans[1::2] = odd

        return ans

