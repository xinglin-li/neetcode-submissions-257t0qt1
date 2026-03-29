class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # function of topo. sort
        def topo_sort(edges):
            indeg = [0]*(k+1)
            graph = defaultdict(list)
            for a,b in edges:
                graph[a].append(b)
                indeg[b] += 1
            
            q = deque(i for i in range(1, k+1) if indeg[i] == 0)
            order = []
            while q:
                a = q.popleft()
                order.append(a)
                for nei in graph[a]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return order if len(order) == k else []
        
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []
        
        row_map = {num:idx for idx, num in enumerate(row_order)}
        col_map = {num:idx for idx, num in enumerate(col_order)}
        res = [[0]*k for _ in range(k)]
        for x in range(1,k+1):
            r = row_map[x]
            c = col_map[x]
            res[r][c] = x
        return res


