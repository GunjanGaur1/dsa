class Solution:
    def largestInteger(self, num: int) -> int:
        result = []
        even = []
        odd = []

        digits = list(str(num))

        for digit in str(num):
            digit = int(digit)
            if digit%2==0:
                even.append(digit)
            else:
                odd.append(digit)
        even.sort()
        odd.sort()
        for digit in digits:
            digit = int(digit)
            if digit % 2 == 0:
                result.append(even.pop())
            else:
                result.append(odd.pop())


        return int("".join(map(str, result)))