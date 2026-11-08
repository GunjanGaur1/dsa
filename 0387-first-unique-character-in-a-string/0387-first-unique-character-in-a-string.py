class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        hash={}
        for i in range(n):
            if s[i] not in hash:
                hash[s[i]] = 1
            else:
                hash[s[i]] += 1
        for i in range(n):
            if hash[s[i]] == 1:
                return i
        return -1