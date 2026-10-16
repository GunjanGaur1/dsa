class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        n = rowIndex
        res = []
        for i in range(n+1):
            curr = []
            curr.append(1)
            if i>=2:
                prev = res[i-1]
                for j in range(0,i-1):
                    curr.append(prev[j]+prev[j+1])
            if i>0:
                curr.append(1)
            res.append(curr)
        return res[rowIndex]