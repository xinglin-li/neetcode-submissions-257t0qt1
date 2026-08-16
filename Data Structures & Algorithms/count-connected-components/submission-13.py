class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union-find. Assume connected components is n, for every two edges, if they are not in the same union
        # we union them and reduce the connected components by 1.

        parent = list(range(n))
        
        # 并查集：带路径压缩的查找
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # 初始时有 n 个独立的连通分量
        components = n
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            # 若两个节点属于不同集合，合并它们并将连通分量数减 1
            if root_u != root_v:
                parent[root_u] = root_v
                components -= 1
                
        return components
