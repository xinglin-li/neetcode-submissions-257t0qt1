"""
Here’s the clean way to think about it:

A graph is a valid tree iff

1) it has exactly n − 1 edges, and

2) it is connected (all nodes reachable from any node).
(With n−1 edges, “connected” also guarantees “acyclic,” and vice-versa.)
"""
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        # find the root of node x
        while x != self.p[x]:
            self.p[x] = self.p[self.p[x]] # halving
            x = self.p[x]
        return x
    def union(self, a,b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        rank_ra, rank_rb = self.r[ra], self.r[rb]
        if rank_ra < rank_rb:
            self.r[ra], self.r[rb] = rank_rb, rank_ra
        if rank_ra == rank_rb:
            self.r[ra] += 1 
        self.p[rb] = ra
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return True

"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = set()
        def dfs(u):
            if u in visited:
                return 
            visited.add(u)
            for v in g[u]:
                dfs(v)
        dfs(0)
        return len(visited) == n
"""
