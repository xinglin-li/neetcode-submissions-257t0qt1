class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            else:
               heapq.heappush_max(stones, abs(x-y))
        return stones[0] if stones else 0  
