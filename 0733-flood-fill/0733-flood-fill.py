class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n = len(image)
        m=len(image[0])
        def dfs(sr,sc):
            if sr<0 or sr>n-1 or sc<0 or sc>m-1:
                return
            if image[sr][sc]==original:
                image[sr][sc]=color
            else:
                return 

            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)

        original = image[sr][sc]
        if original!=color:
            dfs(sr,sc)
        else:
            return image

        return image
            