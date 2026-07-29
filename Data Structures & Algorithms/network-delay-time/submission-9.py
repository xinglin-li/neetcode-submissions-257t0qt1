class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Single-Source Shortest Path, SSSP
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        dist = {i:float("inf") for i in range(1, n+1)}
        dist[k] = 0 #very important
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > dist[node]:
                continue
            for nei, weight in graph[node]:
                new_cost = weight + time
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(min_heap, (new_cost, nei))

        max_delay = max(dist.values())

        return max_delay if max_delay != float("inf") else -1
