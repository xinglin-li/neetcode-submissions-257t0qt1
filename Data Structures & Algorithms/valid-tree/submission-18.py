class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # (1) math trick, valid tree has n - 1 edges. (2) valid tree no cycle, use union-find
        if len(edges) != n-1:
            return False
        
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False
            parent[root_u] = root_v
        
        return True