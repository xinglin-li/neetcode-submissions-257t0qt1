class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {}   # weight[x] = x / parent[x]

        def find(x):
            if parent[x] != x:
                px = parent[x]
                root = find(px)
                parent[x] = root
                weight[x] *= weight[px]   # ⭐ 路径压缩时要更新比例
            return parent[x]

        def union(a, b, val):
            # a / b = val
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                # ⭐ 让 pa 连接到 pb，并更新 pa 的 weight
                # (a/rootA) / (b/rootB) = val
                weight[pa] = val * weight[b] / weight[a]

        # 1️⃣ 初始化 parent 和 weight
        for (a, b), val in zip(equations, values):
            if a not in parent:
                parent[a] = a
                weight[a] = 1.0
            if b not in parent:
                parent[b] = b
                weight[b] = 1.0
            union(a, b, val)

        # 2️⃣ 查询
        res = []
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1.0)
                continue
            pa = find(a)
            pb = find(b)
            if pa != pb:
                res.append(-1.0)
            else:
                res.append(weight[a] / weight[b])
        return res
