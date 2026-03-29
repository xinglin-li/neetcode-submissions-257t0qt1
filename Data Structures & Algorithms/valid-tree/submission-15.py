"""
Here’s the clean way to think about it:

A graph is a valid tree iff

1) it has exactly n − 1 edges, and

2) it is connected (all nodes reachable from any node).
(With n−1 edges, “connected” also guarantees “acyclic,” and vice-versa.)
"""
from typing import List

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.p[self.p[x]]  # path halving
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # cycle found
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):  # union returns False if u and v already connected → cycle
                return False
        return True  # n-1 edges + no cycle ⇒ connected ⇒ tree


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
