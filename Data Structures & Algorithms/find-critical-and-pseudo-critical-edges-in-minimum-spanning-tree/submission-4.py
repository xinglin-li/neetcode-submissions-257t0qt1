class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = []
        for i, (u,v,w) in enumerate(edges):
            new_edges.append([u,v,w,i])
        
        new_edges.sort(key=lambda x:x[2])

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

        def kruskal(skip_edge: int = -1, pick_edge: int = -1) -> int:
            parent = list(range(n))
            rank = [0]*n
            total_weight = 0
            edges_used = 0
            if pick_edge != -1:
                u,v,w,_ = new_edges[pick_edge]
                if union(parent, rank, u,v):
                    total_weight += w
                    edges_used += 1
            for i, (u,v,w,_) in enumerate(new_edges):
                if i == skip_edge:
                    continue
                if union(parent,rank,u,v):
                    total_weight += w
                    edges_used += 1
                    if edges_used == n - 1:
                        break
            if edges_used < n - 1:
                return float('inf')
            return total_weight

        base_weight = kruskal()
        critical = []
        pseudo = []

        for i in range(len(new_edges)):
            weight_without = kruskal(skip_edge=i)
            if weight_without > base_weight:
                critical.append(new_edges[i][3])
            else:
                weight_with = kruskal(pick_edge=i)
                if weight_with == base_weight:
                    pseudo.append(new_edges[i][3])
        return [critical, pseudo]