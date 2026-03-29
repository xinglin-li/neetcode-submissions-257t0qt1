class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i,price_i))

        pq = [(0, src, 0)]
        best = {}
        while pq:
            cost, city, stops = heapq.heappop(pq)
            if city == dst:
                return cost
            if stops > k:
                continue
            if (city, stops) in best and best[(city, stops)] < cost:
                continue
            for nei, price in graph[city]:
                new_cost = cost + price
                state = (nei, stops + 1)
                if state not in best or new_cost < best[state]:
                    heapq.heappush(pq, (new_cost, nei, stops + 1))
        return -1    
