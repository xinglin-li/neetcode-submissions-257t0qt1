class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union-find. 如果发现边的两端在同一个union, 那么该边就是redundant.
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] # path compression
                x = parent[x] # path halving
            return parent[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]