class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n=len(image[0])

        def dfs(i,j):
        
            if i<0 or i>m-1 or j<0 or j>n-1:
                return
            if image[i][j] != original_color:
                return
            image[i][j]=color

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        

        original_color = image[sr][sc]
        if original_color == color:
            return image
        dfs(sr,sc)

        return image