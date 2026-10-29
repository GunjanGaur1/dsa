class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        maxi=0
        left=0
        right=n-1
        while left<right:
            area = (right - left) * min(height[left], height[right])
            maxi = max(maxi,area)
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return maxi