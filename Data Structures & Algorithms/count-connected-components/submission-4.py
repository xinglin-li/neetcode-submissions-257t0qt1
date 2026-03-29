class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
        self.count = n
    def find(self, x):
        while x!=self.p[x]:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    # suppose you want to use DSU, you need to have variant union functions
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra == rb:
            return
        if self.r[ra] < self.r[rb]:
            ra,rb = rb,ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u,v in edges:
            dsu.union(u,v)
        return dsu.count


"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()
        def bfs(u):
            q = deque([u])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
        
        num_search = 0
        for u in range(n):
            if u not in visited:
                bfs(u)
                num_search += 1
        return num_search
"""

"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()

        def dfs(u):
            if u in visited:
                return 
            visited.add(u)
            for v in g[u]:
                dfs(v)
        
        num_search = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                num_search += 1
        
        return num_search
"""        