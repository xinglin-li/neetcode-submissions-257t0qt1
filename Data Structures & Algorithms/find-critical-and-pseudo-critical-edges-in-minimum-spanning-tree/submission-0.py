class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 1. 给每条边加上原始下标 index，方便最后返回
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])

        # 按 weight 排序是 Kruskal 的基本操作
        new_edges.sort(key=lambda x: x[2])

        # ---- Union-Find / DSU ----
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            rx, ry = find(parent, x), find(parent, y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        # ---- 计算 MST 权值的函数 ----
        # skip_edge = 要“删除”的那条边在 new_edges 里的 index（不参加 Kruskal）
        # pick_edge = 要“强制选入”的那条边在 new_edges 里的 index（先加进去）
        def kruskal(skip_edge: int = -1, pick_edge: int = -1) -> int:
            parent = list(range(n))
            rank = [0] * n
            total_weight = 0
            edges_used = 0

            # 如果有强制选的边，先 union 它
            if pick_edge != -1:
                u, v, w, _ = new_edges[pick_edge]
                if union(parent, rank, u, v):
                    total_weight += w
                    edges_used += 1

            # 正常 Kruskal
            for i, (u, v, w, _) in enumerate(new_edges):
                if i == skip_edge:   # 这条边被“删掉”
                    continue
                if union(parent, rank, u, v):
                    total_weight += w
                    edges_used += 1
                    if edges_used == n - 1:
                        break

            # 如果没连成一棵 spanning tree，返回 +∞（表示失败）
            if edges_used < n - 1:
                return float('inf')
            return total_weight

        # 2. 先算出标准 MST 的最小总权值
        base_weight = kruskal()

        critical = []
        pseudo = []

        # 3. 枚举每一条边（按排序后的 new_edges 下标）
        for i in range(len(new_edges)):
            # 3.1 先试着“删掉”这条边：如果 MST 变重或根本连不起来 → critical edge
            weight_without = kruskal(skip_edge=i)
            if weight_without > base_weight:
                critical.append(new_edges[i][3])  # 原始 index
            else:
                # 3.2 再试着“强制选入”这条边：如果还能得到同样的最小权值 → pseudo-critical edge
                weight_with = kruskal(pick_edge=i)
                if weight_with == base_weight:
                    pseudo.append(new_edges[i][3])

        return [critical, pseudo]