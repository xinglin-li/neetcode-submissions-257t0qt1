class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True
            while (
                alive
                and stack
                and stack[-1] > 0
                and asteroid < 0
            ):
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            
            if alive:
                stack.append(asteroid)
        
        return stack


