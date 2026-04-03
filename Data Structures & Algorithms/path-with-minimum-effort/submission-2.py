class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        m, n = len(heights), len(heights[0])
        efforts = [[float("inf")]*n for _ in range(m)]

        pq = [(0,0,0)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while pq:
            effort, r, c = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return effort
            if effort > efforts[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    edge_weight = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, edge_weight)
                    if new_effort < efforts[nr][nc]:
                        heapq.heappush(pq, (new_effort, nr, nc))
                        efforts[nr][nc] = new_effort
        return 0




