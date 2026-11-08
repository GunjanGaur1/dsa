class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n>1:
            if n in seen:
                return False
            total = 0
            seen.add(n)
            while n>0:
                digit = n % 10
                total += digit * digit
                n = n // 10
            n = total
        return True