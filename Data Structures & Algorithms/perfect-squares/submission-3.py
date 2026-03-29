class Solution:
    def numSquares(self, n: int) -> int:
        import math
        squares = [i*i for i in range(1, int(math.isqrt(n)) + 1)]
        level = 0
        queue = {n}

        while queue:
            level += 1
            next_queue = set()

            for x in queue:
                for sq in squares:
                    if x == sq:
                        return level
                    if x < sq:
                        break
                    next_queue.add(x - sq)

            queue = next_queue

        return level