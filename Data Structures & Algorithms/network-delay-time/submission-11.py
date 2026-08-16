class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra + minHeap
        # 1. 构建有向带权的邻接表
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # 2. Dijkstra算法: 记录各节点已经确定的最短距离
        pq = [(0, k)] # (到达当前节点的累计耗时, 节点编号)
        dist = {} # 充当已访问集合 + 最短耗时字典

        while pq:
            time, u = heapq.heappop(pq)

            # 若该节点已被确定过最短路径, 跳过
            if u in dist:
                continue
            
            dist[u] = time

            # 探索邻居
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(pq, (time + w, v))
        
        # 若能覆盖所有n个节点, 则最大耗时即为信号传遍全网的实践, 否则返回-1
        return max(dist.values()) if len(dist) == n else -1


            