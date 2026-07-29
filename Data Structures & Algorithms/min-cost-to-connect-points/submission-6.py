class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim + min-heap
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited.add(node)
            x1, y1 = points[node]
            total_cost += cost

            for nxt in range(n):
                if nxt in visited:
                    continue
                x2, y2 = points[nxt]
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(min_heap, (dist, nxt))
        
        return total_cost
