class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Method 1: DFS/BFS.
        from collections import defaultdict
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        self.count = 0
        for i in range(n):
            if i not in visited:
                self.count += 1
                dfs(i)
        
        return self.count
