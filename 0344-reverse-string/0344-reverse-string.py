class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)
        for i in range(n//2): #4//2 = 2
            left=i
            right=n-1-i #4
            s[left],s[right]=s[right],s[left]
            
        
        