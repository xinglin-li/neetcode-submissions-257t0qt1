class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集判断无向图成环, Union-Find
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] # path compression
                x = parent[x]
            return x
        
        def union(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
                if rank[p1] == rank[p2]:
                    rank[p2] += 1
            return True
        
        for ai, bi in edges:
            if not union(ai,bi):
                return [ai,bi]
