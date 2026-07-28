class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        count = n

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                count -= 1
                parent[root_u] = parent[root_v]

        return count