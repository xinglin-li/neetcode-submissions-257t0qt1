class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford 算法变体 (松弛 k + 1 次)
        prices = [float('inf')]*n
        prices[src] = 0

        for _ in range(k + 1):
            tmp_prices = prices.copy()
            for u, v, p in flights:
                if prices[u] == float('inf'):
                    continue
                # slack
                if prices[u] + p < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + p
            prices = tmp_prices
        
        return prices[dst] if prices[dst] != float('inf') else -1