class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        n = numRows
        res = []
        for i in range(n):
            curr = []
            curr.append(1)
            if i>=2:
                prev = res[i-1]
                for j in range(0,i-1):
                    curr.append(prev[j]+prev[j+1])
            if i>0:
                curr.append(1)
            res.append(curr)
        return res