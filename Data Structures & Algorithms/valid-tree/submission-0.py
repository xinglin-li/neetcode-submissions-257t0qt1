"""
Here’s the clean way to think about it:

A graph is a valid tree iff

1) it has exactly n − 1 edges, and

2) it is connected (all nodes reachable from any node).
(With n−1 edges, “connected” also guarantees “acyclic,” and vice-versa.)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set([0])
        q = deque([0])
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return len(seen) == n  # connected; with n-1 edges ⇒ tree