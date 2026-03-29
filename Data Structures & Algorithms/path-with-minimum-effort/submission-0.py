class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0,0,0)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while pq:
            effort, r, c = heapq.heappop(pq)
            if r == m-1 and c == n-1:
                return effort

            if effort > dist[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <=nr<=m-1 and 0<=nc<=n-1:
                    abs_dist = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort,abs_dist)
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (dist[nr][nc], nr, nc))
        return 0