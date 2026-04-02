class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 特殊边界情况处理
        if n == 1:
            return [0]
        
        # 1. 构建邻接表和度数表 (Degree Array)
        adj = collections.defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # 2. 将所有叶子节点（度数为1的节点）入队
        queue = collections.deque([i for i in range(n) if degree[i] == 1])
        
        # 3. 开始“剥洋葱”
        remaining_nodes = n
        # 只要剩余节点数大于 2，就继续剥
        while remaining_nodes > 2:
            # 当前这一层的叶子节点数量
            leaves_count = len(queue)
            remaining_nodes -= leaves_count
            
            # 把当前层的叶子节点全部剥离
            for _ in range(leaves_count):
                leaf = queue.popleft()
                # 更新与该叶子节点相邻的节点的度数
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    # 如果相邻节点变成了新的叶子节点，加入队列
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        
        # 4. 最后留在队列里的，就是树的中心节点
        return list(queue)




