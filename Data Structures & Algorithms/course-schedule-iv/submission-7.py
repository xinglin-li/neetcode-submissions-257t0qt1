class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 图论经典 Floyd - Warshall 算法 (Dynamic Programming)
        # 1. Initialize Reachable Matrix
        reachable = [[False]*numCourses for _ in range(numCourses)]

        # 2. 填入直接相邻的边 (直接先修关系)
        for u,v in prerequisites:
            reachable[u][v] = True
        
        # 3. Key: 三重循环.
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        return [reachable[u][v] for u,v in queries]