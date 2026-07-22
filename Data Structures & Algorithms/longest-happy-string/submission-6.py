class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))

        res = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break
                
                next_count, next_char = heapq.heappop(max_heap)
                res.append(next_char)

                if next_count + 1 < 0:
                    heapq.heappush(max_heap, (next_count + 1, next_char))
                
                heapq.heappush(max_heap, (count, char))
            else:
                res.append(char)
                if count + 1 < 0:
                    heapq.heappush(max_heap, (count + 1, char))
        
        return "".join(res)
                

