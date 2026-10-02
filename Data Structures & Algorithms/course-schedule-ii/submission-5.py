class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indeg[a] += 1
            adj[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        if len(order) == numCourses:
            return order
        else:
            return []