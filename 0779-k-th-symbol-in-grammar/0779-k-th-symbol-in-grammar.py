class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0

        while k > 1:
            if k % 2 == 0:
                ans = 1 - ans

            k = (k + 1) // 2

        return ans