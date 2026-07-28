class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # peel the onion
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

        remaining_node = n
        while remaining_node > 2:
            num_leaf = len(q)
            remaining_node -= num_leaf
            for _ in range(num_leaf):
                node = q.popleft()
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 1:
                        q.append(nei)
        
        return list(q)