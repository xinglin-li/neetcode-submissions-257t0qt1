class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 拓扑排序：对 1 到 k 的数字排出一个满足条件的线性序列
        def topo_sort(edges):
            adj = defaultdict(list)
            in_degree = [0] * (k + 1)
            for u, v in edges:
                adj[u].append(v)
                in_degree[v] += 1
            q = deque([i for i in range(1, k+1) if in_degree[i] == 0])
            order = []

            while q:
                curr = q.popleft()
                order.append(curr)
                for nei in adj[curr]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        q.append(nei)
            return order if len(order) == k else []

        # 1. 分别对行约束和列约束做拓扑排序
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []
        
        row_pos = {num:i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        # 4. 初始化 k x k 矩阵并填充数字
        ans = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            ans[r][c] = num

        return ans