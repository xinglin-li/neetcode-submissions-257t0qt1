class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        标准答案：BFS (Kahn 算法)
        (1) 每次只去上那些没有先修课要求的课（即“入度”为 0 的节点）。
        (2) 上完一门课后，把这门课作为先修课的所有后续课程的依赖解除掉（将后续节点的“入度”减 1）。
        (3) 如果后续课程的依赖也全部解除（入度变成 0），就把它加入可修课程的队列中。
        (4) 最后检查修完的课程总数是否等于 numCourses。
        """
        indeg = [0] * (numCourses)
        neighbors = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indeg[a] += 1
            neighbors[b].append(a)

        q = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            for nei in neighbors[course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return sum(indeg) == 0



        
