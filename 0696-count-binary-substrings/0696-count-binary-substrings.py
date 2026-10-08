class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        current = 1
        prev = 0
        for i in range(1,n):
            if s[i]==s[i-1]:
                current = current + 1
            else:
                ans = ans + min(current,prev)
                prev = current
                current = 1
        ans = ans + min(current,prev)
        return ans



# brute force approach
#         ans = 0
#         changes = 0
# 
#         for i in range(n):
#             count0 = 0
#             count1 = 0
#             changes = 0
# 
#             for j in range(i, n):
#                 if s[j] == "0":
#                     count0 = count0 + 1
#                 elif s[j] == "1":
#                     count1 = count1 + 1
# 
#                 if j > i and s[j] != s[j - 1]:
#                     changes = changes + 1
# 
#                 if changes == 1 and count0 == count1:
#                     ans = ans + 1
# 
#         return ans
