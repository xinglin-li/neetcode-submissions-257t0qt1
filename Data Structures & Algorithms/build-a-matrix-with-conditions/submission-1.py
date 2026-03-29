class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological sort function
        def topo_sort(edges):
            graph = defaultdict(list)
            indeg = [0] * (k + 1)
            
            for a, b in edges:
                graph[a].append(b)
                indeg[b] += 1
            
            q = deque([i for i in range(1, k + 1) if indeg[i] == 0])
            order = []
            
            while q:
                x = q.popleft()
                order.append(x)
                for nei in graph[x]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            
            return order if len(order) == k else []  # If cycle → no solution
        
        # 1. row order
        rowOrder = topo_sort(rowConditions)
        # 2. col order
        colOrder = topo_sort(colConditions)
        
        if not rowOrder or not colOrder:
            return []  # impossible
        
        # 3. Map position
        rowPos = {x: i for i, x in enumerate(rowOrder)}
        colPos = {x: i for i, x in enumerate(colOrder)}
        
        # 4. Build matrix
        res = [[0] * k for _ in range(k)]
        
        for x in range(1, k + 1):
            r = rowPos[x]
            c = colPos[x]
            res[r][c] = x
        
        return res

