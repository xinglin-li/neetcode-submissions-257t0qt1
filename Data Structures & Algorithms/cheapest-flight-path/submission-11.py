class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS Level Search
        adj = collections.defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
            
        # dist 数组记录到达每个节点的最小花费，用于剪枝
        dist = [float('inf')] * n
        dist[src] = 0
        
        # 队列中存储：(当前节点, 当前总花费)
        queue = collections.deque([(src, 0)])
        stops = 0
        
        # BFS 按层遍历，最多执行 k + 1 层
        while queue and stops <= k:
            size = len(queue)
            for _ in range(size):
                curr_node, curr_price = queue.popleft()
                
                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    # 只有当新路径更便宜时，才更新并入队
                    if new_price < dist[neighbor]:
                        dist[neighbor] = new_price
                        queue.append((neighbor, new_price))
            stops += 1
            
        return dist[dst] if dist[dst] != float('inf') else -1


