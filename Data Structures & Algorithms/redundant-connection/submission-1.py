class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集判断无向图成环, Union-Find
        # Union-Find initialization
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # already connected → this edge causes cycle
            
            if rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1
            return True
        
        # Process edges
        for a, b in edges:
            if not union(a, b):
                return [a, b]   # the first edge that forms a cycle
        
        for ai, bi in edges:
            if not union(ai,bi):
                return [ai,bi]
