class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # construct a MST.
        n = len(points)
        in_mst = [False]*n
        pq = [(0,0)] # cost, node
        total_cost = 0
        edge = 0
        while pq and edge < n:
            cost, node = heapq.heappop(pq)
            if in_mst[node]:
                continue
            in_mst[node] =True
            total_cost += cost
            edge += 1
            xi, yi = points[node]
            for j in range(n):
                if not in_mst[j]:
                    xj, yj = points[j]
                    dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(pq, (dist, j))
        return total_cost

