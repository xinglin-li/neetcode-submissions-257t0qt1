class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(list)
        degree = [0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        q = deque(i for i in range(n) if degree[i] == 1)
        remainding_nodes = n

        while remainding_nodes > 2:
            remainding_nodes -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        return list(q)


