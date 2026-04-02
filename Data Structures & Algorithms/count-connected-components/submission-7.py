class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. 构建邻接表
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        count = 0
        
        # 2. 定义 DFS 遍历逻辑
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        # 3. 遍历所有节点
        for i in range(n):
            if i not in visited:
                count += 1           # 发现新的连通分量
                visited.add(i)       # 标记当前节点
                dfs(i)               # 找出所有同属一个分量的节点
                
        return count
