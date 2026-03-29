class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        learned = 0
        while q:
            course = q.popleft()
            learned += 1
            for c in graph[course]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)
        return learned == numCourses
