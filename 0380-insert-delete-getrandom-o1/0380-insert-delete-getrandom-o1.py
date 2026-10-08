import random

class RandomizedSet:

    def __init__(self):
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False

        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False

        self.nums.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)