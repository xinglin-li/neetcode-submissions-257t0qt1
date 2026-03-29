class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # adjacency list
        g = defaultdict(list)
        indeg = [0] * numCourses
        
        for a, b in prerequisites:
            g[a].append(b)
            indeg[b] += 1
        
        # BFS topological order
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            x = q.popleft()
            topo.append(x)
            for nxt in g[x]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        
        # reachable[i][j] = i 是 j 的 prerequisite
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # DP 传递闭包 (顺拓扑结果保证方向正确)
        for x in topo:
            for nxt in g[x]:
                # nxt inherits all prereqs of x
                for k in range(numCourses):
                    if reachable[k][x]:
                        reachable[k][nxt] = True
        
        # answer queries
        ans = []
        for u, v in queries:
            ans.append(reachable[u][v])
        
        return ans
