class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS Topological Sort. In practice, bfs is more suitible for topological sort.
        from collections import deque, defaultdict
        indeg = [0]*numCourses
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indeg[crs] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indeg[crs] == 0:
                q.append(crs)
        
        order = []

        while q:
            crs = q.popleft()
            order.append(crs)
            for nei in graph[crs]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return order if len(order) == numCourses else []
        
