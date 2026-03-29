class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)

        # dist[r][c] = 从 (0,0) 到 (r,c) 的最小“最大高度”
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        # 最小堆： (当前路径上的最大高度, r, c)
        pq = [(grid[0][0], 0, 0)]

        # 4 个方向
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            time, r, c = heapq.heappop(pq)

            # 如果已经到终点，这是可能的最小时间，直接返回
            if r == n - 1 and c == n - 1:
                return time

            # 剪枝：如果现在的 time 比记录的大，说明这条路已经不是最优的
            if time > dist[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # 走到邻居需要的水位：当前路径上的最大高度 vs 邻居高度
                    new_time = max(time, grid[nr][nc])
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))
