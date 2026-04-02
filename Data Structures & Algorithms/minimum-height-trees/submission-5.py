class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        indeg = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        q = deque()
        for i in range(n):
            if indeg[i] == 1:
                q.append(i)

        node_left = n
        while node_left>2:
            level_len = len(q)
            node_left -= level_len
            for _ in range(level_len):
                node = q.popleft()
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 1:
                        q.append(nei)
        
        return list(q)




