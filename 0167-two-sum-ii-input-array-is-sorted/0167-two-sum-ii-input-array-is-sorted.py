class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        hash = {}
        for i in range(n):
            compliment = target-numbers[i]
            if compliment in hash:
                return [hash[compliment]+1,i+1]
            hash[numbers[i]] = i