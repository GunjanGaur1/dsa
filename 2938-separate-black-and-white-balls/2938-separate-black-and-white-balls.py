class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        n = len(s)
        swap=0
        for i in range(n):
            if s[i]=='1':
                count=count+1
            else:
                swap = swap + count
        return swap
