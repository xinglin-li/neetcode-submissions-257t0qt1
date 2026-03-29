class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            elif stack[-1] < 0:
                stack.append(asteroid)
            elif asteroid < 0 and stack[-1] > 0:
                while stack and abs(asteroid) > abs(stack[-1]) and stack[-1] >0:
                    stack.pop()
                if not stack:
                    stack.append(asteroid)
                elif abs(asteroid) == abs(stack[-1]) and stack[-1] >0:
                    stack.pop()
                elif stack[-1] < 0 and asteroid < 0:
                    stack.append(asteroid)
                else:
                    continue
            else:
                stack.append(asteroid)
        return stack