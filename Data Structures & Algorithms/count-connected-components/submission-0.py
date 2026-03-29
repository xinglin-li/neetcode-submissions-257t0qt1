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
        