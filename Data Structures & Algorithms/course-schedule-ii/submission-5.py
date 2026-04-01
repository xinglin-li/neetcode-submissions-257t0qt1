class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 初始化入度表和邻接表
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        
        # 2. 建图 (注意：题目中 [a, b] 表示修 a 之前必须修 b，即 b -> a)
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
            
        # 3. 初始化队列，将所有入度为 0 (没有先决条件) 的课程入队
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
                
        # 4. 执行 BFS 并记录出队顺序
        result_order = []  # 核心改动：用数组记录具体的修课路径
        
        while queue:
            node = queue.popleft()
            result_order.append(node)  # 将当前课程加入修课顺序
            
            # 遍历修完这门课后解锁的后续课程
            for neighbor in adjacency[node]:
                indegrees[neighbor] -= 1  # 消除一层依赖
                
                # 如果依赖全部消除，加入队列
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 5. 检查是否所有的课都修完了
        if len(result_order) == numCourses:
            return result_order
        else:
            return []  # 存在环，课程互相依赖，返回空数组

