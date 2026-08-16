class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 有效树的充要条件：
        # 1. 边的数量必须恰好等于 n - 1
        # 2. 图中无环且所有节点连通
        if len(edges) != n - 1:
            return False
            
        parent = list(range(n))
        
        # 并查集查找（带路径压缩）
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        # 并查集合并
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # 如果两个节点已经在同一连通分量中，加入该边会形成环
            if root_u == root_v:
                return False
            parent[root_u] = root_v
            
        return True

