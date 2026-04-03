class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v,p))
        dist = [float("inf")]*n
        dist[src] = 0
        q = deque([(src,0)])
        level = 0
        while q and level <= k:
            len_level = len(q)
            level += 1
            for _ in range(len_level):
                node, price = q.popleft()
                for nei, cost in graph[node]:
                    new_cost = price + cost
                    if dist[nei] > new_cost:
                        dist[nei] = new_cost
                        q.append((nei,new_cost))
        return dist[dst] if dist[dst] != float("inf") else -1


