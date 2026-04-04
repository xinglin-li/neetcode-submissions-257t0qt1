class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # ==========================================
        # 核心模板：Kahn's Algorithm 拓扑排序
        # ==========================================
        def topo_sort(conditions):
            graph = defaultdict(list)
            in_degree = [0] * (k + 1) # 数字从 1 到 k
            
            # 1. 建图并统计入度
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
                
            # 2. 初始化队列，将所有入度为 0 的节点（即没有前置条件的节点）入队
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            order = []
            
            # 3. BFS 剥洋葱式排查
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1 # 拆除一条依赖边
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                        
            # 4. 判环：如果排出来的元素个数不等于 k，说明图中有环（逻辑死锁）
            return order if len(order) == k else []

        # ==========================================
        # 主逻辑
        # ==========================================
        
        # 第一步：独立计算行号和列号的拓扑序
        row_order = topo_sort(rowConditions)
        # 如果行条件自相矛盾，直接返回空
        if not row_order: 
            return []
            
        col_order = topo_sort(colConditions)
        # 如果列条件自相矛盾，直接返回空
        if not col_order: 
            return []
            
        # 第二步：将排列好的数组转换为“数字到索引”的哈希表，方便 $O(1)$ 查找坐标
        # 例如 row_order = [3, 1, 2]，那么 row_pos[3]=0, row_pos[1]=1, row_pos[2]=2
        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: i for i, val in enumerate(col_order)}
        
        # 第三步：组装最终的 k * k 矩阵
        matrix = [[0] * k for _ in range(k)]
        for val in range(1, k + 1):
            # 获取数字 val 应该在的行坐标和列坐标
            r = row_pos[val]
            c = col_pos[val]
            # 填入矩阵
            matrix[r][c] = val
            
        return matrix

