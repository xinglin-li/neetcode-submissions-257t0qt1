class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union-find. Assume connected components is n, for every two edges, if they are not in the same union
        # we union them and reduce the connected components by 1.

        parent = [i for i in range(n)]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        self.count = n
        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                self.count -= 1
        
        for a,b in edges:
            union(a,b)
        
        return self.count
