class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
# 1. 构建带权有向图
        # graph[u][v] 表示 u / v 的值
        graph = collections.defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        # 2. 定义 DFS 来寻找从 start 到 target 的路径乘积
        def dfs(start, target, visited):
            # 如果变量根本不存在于图中
            if start not in graph or target not in graph:
                return -1.0
            # 找到了目标
            if start == target:
                return 1.0
            
            visited.add(start)
            # 遍历邻居
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    # 递归寻找路径
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res # 路径上的权重相乘
            
            return -1.0

        # 3. 处理所有查询
        ans = []
        for u, v in queries:
            ans.append(dfs(u, v, set()))
            
        return ans

