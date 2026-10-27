class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count=0
        last_count=0

        for i in range(n):
            if s[i]!=" ":
                count = count + 1
            else:
                if count>0:
                    last_count = count
                count = 0
        if count>0:
            last_count = count
        return last_count