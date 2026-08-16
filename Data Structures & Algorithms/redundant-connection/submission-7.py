class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find. 如果发现边的两端在同一个union, 那么该边就是redundant.
        n = len(edges)
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # 若两个端点已在同一连通分量中，再连此边必产生环，该边即为冗余边
            if root_u == root_v:
                return [u, v]
            # 合并连通分量
            parent[root_u] = root_v
            
        return []