class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        prev = 0
        curr = 1
        ans = 0
        for i in range(n-1):
            if s[i]==s[i+1]:
                ##print("i is",i)
                curr = curr + 1
                ##print("current is:==",curr)         
            else:
                ans = ans + min(curr, prev)
                ##print("ans",ans)
                ##print("i is",i)
                prev = curr 
                curr = 1
        ans = ans + min(curr,prev)
        ##print("ans is:==",ans)
        return ans 
