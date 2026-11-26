class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n=len(heights)
        maxi = float('-inf')
        ans = []
        for i in range(n-1, -1, -1):
            if heights[i]>maxi:
                ans.append(i)
                maxi=heights[i]
        return ans[::-1]


