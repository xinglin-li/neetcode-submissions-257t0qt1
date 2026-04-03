class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # 记录节点是否已经被拉入到“最小生成树”中
        in_mst = [False] * n
        
        # 优先队列：存放 (距离, 目标节点编号)
        # 我们随便挑一个点作为整棵树的生长起点，比如点 0
        min_heap = [(0, 0)]
        
        total_cost = 0
        edges_used = 0
        
        # 当堆不为空，且还没把所有节点都拉入树中时
        while min_heap and edges_used < n:
            cost, u = heapq.heappop(min_heap)
            
            # 剪枝：如果这个节点已经在树里了，说明这是一条冗余的边，跳过
            if in_mst[u]:
                continue
                
            # 正式将节点 u 拉入树中
            in_mst[u] = True
            total_cost += cost
            edges_used += 1
            
            # 遍历所有还没进树的节点 v，计算它们到新节点 u 的曼哈顿距离
            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    # 把潜在的边塞入堆中，让堆去自动帮我们挑出下一条最短的边
                    heapq.heappush(min_heap, (dist, v))
                    
        return total_cost

