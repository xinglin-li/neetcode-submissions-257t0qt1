class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        indeg = [0]*numCourses
        downstreams = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            indeg[a] += 1
            downstreams[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            for dc in downstreams[course]:
                indeg[dc] -= 1
                if indeg[dc] == 0:
                    q.append(dc)
        return order if len(order) == numCourses else []

