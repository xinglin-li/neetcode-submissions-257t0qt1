class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # (1) math trick, valid tree has n - 1 edges. (2) valid tree no cycle, use union-find
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            parent[pu] = pv
        
        return True

