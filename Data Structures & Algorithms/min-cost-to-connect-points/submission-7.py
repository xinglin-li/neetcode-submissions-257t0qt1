class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # min_dist[i]:
        # 当前生成树连接到点 i 的最低成本
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            # 1. 找到未访问点中，连接成本最低的点
            curr = -1

            for i in range(n):
                if not visited[i] and (
                    curr == -1 or min_dist[i] < min_dist[curr]
                ):
                    curr = i

            # 2. 将当前点加入最小生成树
            visited[curr] = True
            total_cost += min_dist[curr]

            # 3. 用当前点更新其他未访问点的最低连接成本
            x1, y1 = points[curr]

            for nxt in range(n):
                if visited[nxt]:
                    continue

                x2, y2 = points[nxt]
                distance = abs(x1 - x2) + abs(y1 - y2)

                min_dist[nxt] = min(min_dist[nxt], distance)

        return total_cost
