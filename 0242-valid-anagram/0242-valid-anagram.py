class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        hash1 = {}
        n = len(s)
        m = len(t)
        for i in range(n):
            if s[i] not in hash:
                hash[s[i]] =1
            else:
                hash[s[i]] =hash[s[i]]+1
        for i in range(m):
            if t[i] not in hash1:
                hash1[t[i]] =1
            else:
                hash1[t[i]] =hash1[t[i]]+1
        
        return hash == hash1
