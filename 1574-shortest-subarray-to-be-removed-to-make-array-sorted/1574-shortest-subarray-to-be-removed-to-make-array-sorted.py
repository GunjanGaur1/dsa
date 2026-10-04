class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr) #8
        i = 0
        j = n-1
        print(j)
        
        while i+1<n and arr[i+1]>=arr[i]:
            i = i + 1
            print(i)
        if i == n - 1:
            return 0
        
        while j>0 and arr[j]>=arr[j-1]:
            j = j - 1
            print(j)
        # the boundary ..

        # my approach here ..
        l = 0 
        r = j
        ans = min(n - i - 1, j) ## changes made here ..
        while l<=i and r<n:
            if arr[l]<=arr[r]:
                ans = min(ans, r-l-1)
                l =  l + 1
            else:
                r = r + 1

        return ans

        