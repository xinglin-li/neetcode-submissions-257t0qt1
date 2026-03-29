"""
Here’s the clean way to think about it:

A graph is a valid tree iff

1) it has exactly n − 1 edges, and

2) it is connected (all nodes reachable from any node).
(With n−1 edges, “connected” also guarantees “acyclic,” and vice-versa.)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([0])
        visited = set([0])
        while q:
            u =q.popleft()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return len(visited) == n