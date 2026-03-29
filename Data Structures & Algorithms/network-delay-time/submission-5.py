import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra + Min Heap
        # adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # min heap: (distance, node)
        heap = [(0, k)]
        # dist array: initialize as infinity
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        while heap:
            cur_dist, node = heapq.heappop(heap)

            # If current path is worse than recorded one, skip
            if cur_dist > dist[node]:
                continue

            # Relax edges
            for nei, w in graph[node]:
                new_dist = cur_dist + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        # 最终答案：所有节点中最大 dist 值，就是传播完需要的时间
        res = max(dist.values())
        return res if res < float('inf') else -1

            


