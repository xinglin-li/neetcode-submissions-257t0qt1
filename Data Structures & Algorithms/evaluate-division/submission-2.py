class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # directed, weighted graph
        graph = defaultdict(list)
        for (a,b), val in zip(equations, values):
            graph[a].append((b,val))
            graph[b].append((a,1/val))
        
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1
            q = deque([(src,1.0)])
            visited = set()
            while q:
                node, acc = q.popleft()
                if node == dst:
                    return acc
                for nei,val in graph[node]:
                    if nei in visited: continue
                    q.append((nei, acc*val))
                    visited.add(nei)
            return -1.0
        return [bfs(src,dst) for src, dst in queries]