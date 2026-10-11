class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            current = asteroids[i]
            while stack and stack[-1]>0 and current<0:
                if -current>stack[-1]:
                    stack.pop()
                elif -current<stack[-1]:
                    current = 0
                else:
                    current = 0
                    stack.pop()
            if current!=0:
                stack.append(current)

        return stack
