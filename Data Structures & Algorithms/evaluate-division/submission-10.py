class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Union - Find solution
        # Union - Find with weights
        parent = {}
        weight = {}
        def find(x):
            if parent[x] != x:
                px = parent[x]
                root = find(px)
                parent[x] = root
                weight[x] *= weight[px]
            return parent[x] 
        
        def union(a,b,val):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                # val = a/b, we want weight[pa] = pa/pb
                # weight[a] = a/pa, weight[b] = b/pb, weight[b]/weight[a]=(b/a)*(pa/pb)
                weight[pa] = val*weight[b]/weight[a]
        
        for (a,b), val in zip(equations, values):
            if a not in parent:
                parent[a] = a
                weight[a] = 1.0
            if b not in parent:
                parent[b] = b
                weight[b] = 1.0
            union(a,b,val)
        res = []
        for a,b in queries:
            if a not in parent or b not in parent:
                res.append(-1.0)
                continue
            pa = find(a)
            pb = find(b)
            if pa != pb:
                res.append(-1.0)
            else:
                res.append(weight[a]/weight[b])
        return res
            
            
                