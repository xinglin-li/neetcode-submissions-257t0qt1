class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra + Min Heap， O(ElogV)
        from collections import deque
        import heapq
        graph = defaultdict(list)
        for u, v , w in times:
            graph[u].append((v,w))
        
        heap = [(0,k)]
        dist = {i: float('inf') for i in range(1,n+1)}
        dist[k] = 0

        while heap:
            cur_dist, node = heapq.heappop(heap)
            if cur_dist > dist[node]:
                continue
            for nei, w in graph[node]:
                new_dist = cur_dist + w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap,(new_dist,nei))
        res = max(dist.values())
        return res if res < float('inf') else -1

            


