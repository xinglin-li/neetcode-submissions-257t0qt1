class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. 建图：构建邻接表
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components = 0

        # 2. 遍历每个节点
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)  # 触发一次 DFS 将当前连通分量的所有节点标记为已访问
                components += 1

        return components