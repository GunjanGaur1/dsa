class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        low = 0
        high = m*n-1
        while low<=high:
            mid = (low+high)//2

            row = mid//m
            col = mid%m
            if matrix[row][col]==target:
                return True 
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False