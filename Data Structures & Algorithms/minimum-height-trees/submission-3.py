class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 特判
        if n <= 2:
            return [i for i in range(n)]
        
        # 建图 + 度数统计
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # 初始化第一层叶子
        leaves = deque(i for i in range(n) if degree[i] == 1)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            layer_size = len(leaves)
            remaining_nodes -= layer_size
            
            for _ in range(layer_size):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
        
        # 剩下的 1~2 个点就是所有 MHT 的根
        return list(leaves)


