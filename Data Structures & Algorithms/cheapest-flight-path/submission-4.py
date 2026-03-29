class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        # (price, city, stops_used)
        pq = [(0, src, 0)]

        # best[city][stops] = minimum cost to reach city with stops_used
        best = {}
        
        while pq:
            cost, city, stops = heapq.heappop(pq)

            # If we reach dst, return immediately (Dijkstra guarantee)
            if city == dst:
                return cost

            # If used more than k stops, cannot continue
            if stops > k:
                continue

            # Avoid revisiting more expensive states
            if (city, stops) in best and best[(city, stops)] < cost:
                continue

            for nei, price in graph[city]:
                new_cost = cost + price
                state = (nei, stops + 1)

                if state not in best or new_cost < best[state]:
                    best[state] = new_cost
                    heapq.heappush(pq, (new_cost, nei, stops + 1))

        return -1
