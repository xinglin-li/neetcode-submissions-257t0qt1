class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # 记录连通分量的个数
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # 按秩合并优化
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.count -= 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # 1. 记录每条边的原始索引，并按权重升序排序
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])
        
        # 2. 计算基准最小生成树的权重
        uf_std = UnionFind(n)
        std_weight = 0
        for u, v, w, i in edges:
            if uf_std.union(u, v):
                std_weight += w
                
        critical = []
        pseudo_critical = []
        
        # 3. 遍历每一条边，测试其身份
        for u, v, w, i in edges:
            # --- 测试是否为关键边 ---
            uf_ignore = UnionFind(n)
            ignore_weight = 0
            for eu, ev, ew, ei in edges:
                if ei != i and uf_ignore.union(eu, ev):
                    ignore_weight += ew
            
            # 如果图不连通了 (count > 1) 或者 权重增加了
            if uf_ignore.count > 1 or ignore_weight > std_weight:
                critical.append(i)
                continue # 是关键边就不用测试伪关键边了
                
            # --- 测试是否为伪关键边 ---
            uf_force = UnionFind(n)
            uf_force.union(u, v) # 强行优先加入这条边
            force_weight = w
            for eu, ev, ew, ei in edges:
                if uf_force.union(eu, ev):
                    force_weight += ew
                    
            # 如果强行加入后，权重依然等于基准权重
            if force_weight == std_weight:
                pseudo_critical.append(i)
                
        return [critical, pseudo_critical]
            


        