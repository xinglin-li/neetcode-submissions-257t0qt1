class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS Topological Sort. In practice, bfs is more suitible for topological sort.
        from collections import deque, defaultdict
        # Build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # queue of all nodes with indegree 0
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while q:
            node = q.popleft()
            order.append(node)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # if we used all courses, return order; otherwise cycle → impossible
        return order if len(order) == numCourses else []
        
