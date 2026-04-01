class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        标准答案：BFS (Kahn 算法)
        (1) 每次只去上那些没有先修课要求的课（即“入度”为 0 的节点）。
        (2) 上完一门课后，把这门课作为先修课的所有后续课程的依赖解除掉（将后续节点的“入度”减 1）。
        (3) 如果后续课程的依赖也全部解除（入度变成 0），就把它加入可修课程的队列中。
        (4) 最后检查修完的课程总数是否等于 numCourses。
        """
        from collections import deque

        indeg = [0]*numCourses
        downstreams = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indeg[a] += 1
            downstreams[b].append(a)
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        count = 0
        while q:
            course = q.popleft()
            count += 1
            for dc in downstreams[course]:
                indeg[dc] -= 1
                if indeg[dc] == 0:
                    q.append(dc)
        return count == numCourses

        
