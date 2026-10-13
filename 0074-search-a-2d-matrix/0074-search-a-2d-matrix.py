class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix) ##3
        n = len(matrix[0])##4

        low = 0 
        high = m*n-1 ##11

        while low<=high:
            mid = (low+high)//2
            #mid = 11/2 - 5
            row = mid//n ##5//2 - > 1
            col = mid%n  ##5%2 -> 1

            if matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                return True
        return False
 



        