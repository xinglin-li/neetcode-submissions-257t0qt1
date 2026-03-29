class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        heap = []
        if a > 0: heap.append((-a, "a"))
        if b > 0: heap.append((-b, "b"))
        if c > 0: heap.append((-c, "c"))

        heapq.heapify(heap)
        res = []
        while heap:
            count1, char1 = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                res.append(char2)
                if count2 < -1:
                    heapq.heappush(heap, (count2 + 1, char2))
                heapq.heappush(heap, (count1, char1))
            else:
                res.append(char1)
                if count1 < -1:
                    heapq.heappush(heap, (count1 + 1, char1))
        return "".join(res)

                
