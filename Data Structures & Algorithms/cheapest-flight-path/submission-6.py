class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford
# prices[i] 记录从 src 到 i 的最小花费
        prices = [float('inf')] * n
        prices[src] = 0
        
        # 允许 k 次中转，相当于最多乘坐 k+1 次航班（走 k+1 条边）
        for _ in range(k + 1):
            # 必须使用一个临时数组来记录上一轮的状态
            # 否则一轮循环中可能会发生“连续转机”的串联更新，破坏了步数限制
            tmp_prices = prices.copy()
            
            for u, v, price in flights:
                # 如果起点 u 都还没能到达，跳过
                if prices[u] == float('inf'):
                    continue
                
                # 状态转移：到达 v 的新花费 = 上一轮到达 u 的花费 + 从 u 到 v 的机票钱
                if prices[u] + price < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + price
                    
            prices = tmp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1
