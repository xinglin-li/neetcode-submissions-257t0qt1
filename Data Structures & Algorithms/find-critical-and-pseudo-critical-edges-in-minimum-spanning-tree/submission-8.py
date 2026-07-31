class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -=1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal's algorithm, 排序 + 并查集（Union-Find), 先把所有边排序，按顺序遍历边；如果边的两个端点不在同一个集合里，就用并查集 union 起来。
        # Prim's algorithm, 工具：小顶堆 / 优先队列（Min-Heap）。逻辑：维持一个候选边堆，每次从堆里弹出现在能连到的最便宜的边，加入新节点后，再把这个新节点能延伸出的新边压入堆中。
        # 稠密图用Prim. 像这种给出了有限候选边的用Kruskal.
        # 1. 记录每条边的原始索引，并按权重从小到大排序
        # edge 格式: [u, v, weight, original_index]
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])
        new_edges.sort(key=lambda x: x[2])

        # 辅助函数：计算 MST 权重
        def get_mst_weight(ignore_idx = -1, force_idx = -1):
            uf = UnionFind(n)
            total_weight = 0
            if force_idx != -1:
                u, v, w = edges[force_idx]
                uf.union(u, v)
                total_weight += w
            for u, v, w, idx in new_edges:
                if idx == ignore_idx:
                    continue
                if uf.union(u, v):
                    total_weight += w
            return total_weight if uf.count == 1 else float('inf')
        
        # 2. 计算基准 MST 权重
        base_weight = get_mst_weight()
        critical = []
        pesudo_critial = []

        for i in range(len(edges)):
            if get_mst_weight(ignore_idx = i) > base_weight:
                critical.append(i)
            elif get_mst_weight(force_idx = i) == base_weight:
                pesudo_critial.append(i)
        
        return [critical, pesudo_critial]

