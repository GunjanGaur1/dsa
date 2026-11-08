class Solution:
    def addDigits(self, num: int) -> int:
        seen = set()
        while num>=10:
            total = 0
            while num>0:
                digit = num % 10
                total += digit 
                num = num // 10
            num = total
        return num