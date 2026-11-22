class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b = 0, 1

        while True:
            c = a + b

            if a + b + c == n:
                return True

            if a + b + c > n:
                return False

            a, b = b, c