class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra. Greedy, bfs, updating cost of nodes. Only works for non-neg edge weighted graph.
        m, n = len(heights), len(heights[0])

        dist = [[float('inf')]*(n) for _ in range(m)]
        dist[0][0] = 0

        min_heap = [(0, 0, 0)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if (r,c) == (m-1, n-1):
                return effort
            if effort > dist[r][c]:
                continue
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if next_effort < dist[nr][nc]:
                        dist[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))
    