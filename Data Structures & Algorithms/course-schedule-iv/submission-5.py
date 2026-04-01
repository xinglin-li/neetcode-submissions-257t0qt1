class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import deque
        downstreams = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            downstreams[a].append(b)
        
        reachable = [set() for _ in range(numCourses)]

        for i in range(numCourses):
            q = deque([i])
            visited = set([i])
            while q:
                course = q.popleft()
                for dc in downstreams[course]:
                    if dc not in visited:
                        visited.add(dc)
                        reachable[i].add(dc)
                        q.append(dc)
        
        return [v in reachable[u] for u,v in queries]