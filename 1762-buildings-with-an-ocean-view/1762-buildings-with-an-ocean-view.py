class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        max_height = 0
        result = []
        for i in range(n-1,-1,-1):
            if heights[i]>max_height:
                result.append(i)
                max_height = heights[i]
        return result[::-1]

