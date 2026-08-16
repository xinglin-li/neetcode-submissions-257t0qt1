class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford 算法变体 (松弛 k + 1 次)
        prices = [float('inf')] * n
        prices[src] = 0

        # 最多经过k个中转站, 等价于最多走 k + 1条边
        for _ in range(k + 1):
            # 使用上一轮状态的副本，防止在同一次迭代中连续传递多条边
            tmp_prices = prices.copy()
            
            for u, v, p in flights:
                if prices[u] == float('inf'):
                    continue
                # 松弛操作
                if prices[u] + p < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + p
            
            prices = tmp_prices
        
        return prices[dst] if prices[dst] != float('inf') else -1