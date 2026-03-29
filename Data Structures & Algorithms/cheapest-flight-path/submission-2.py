class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for from_i, to_i, price_i in flights:
            graph[from_i].append((price_i, to_i))
        
        minheap = [[0,src,-1]]
        min_cost = [float('inf')]*n
        min_cost[0] = 0
        while minheap:
            cost_i, src_i, stop_i = heapq.heappop(minheap)
            if stop_i > k:
                continue
            if src_i == dst:
                return cost_i   
            for price_nei, nei in graph[src_i]:
                stop_nei = stop_i + 1
                if stop_nei > k: continue
                cost_nei = price_nei + cost_i
                #if min_cost[nei] < cost_nei: continue
                min_cost[nei] = cost_nei
                heapq.heappush(minheap,(cost_nei,nei,stop_nei))

        return -1


