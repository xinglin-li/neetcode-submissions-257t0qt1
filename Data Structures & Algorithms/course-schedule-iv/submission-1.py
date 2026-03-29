class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        res = [[False]*numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            res[a][b] = True
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        order = []
        while q:
            a = q.popleft()
            order.append(a)
            for b in graph[a]:
                indeg[b] -= 1
                if indeg[b] == 0:
                    q.append(b) 
        
        for a in order:
            for prev_a in range(numCourses):
                if res[prev_a][a]:
                    for b in graph[a]:
                        res[prev_a][b] = True

        return [res[i][j] for i,j in queries]
