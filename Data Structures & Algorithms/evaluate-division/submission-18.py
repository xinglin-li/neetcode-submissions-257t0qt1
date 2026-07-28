class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # cosntruct directed graph with weight
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0/val
        
        def dfs(start, target, visited):
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0
            
            visited.add(start)

            for nei, w in graph[start].items():
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.0:
                        return res*w
            return -1.0
        
        ans = []
        for u,v in queries:
            ans.append(dfs(u,v,set()))
        
        return ans

        
