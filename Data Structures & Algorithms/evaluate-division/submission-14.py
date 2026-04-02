class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {} # weight[x] = x / parent[x]
        
        # 查找根节点，并进行带权路径压缩
        def find(x):
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
                return x
            
            if parent[x] != x:
                origin_parent = parent[x]
                # 递归找到最终的根节点
                parent[x] = find(parent[x])
                # 更新当前节点的权重: x/root = (x/old_parent) * (old_parent/root)
                weight[x] *= weight[origin_parent]
                
            return parent[x]
            
        # 合并两个集合
        def union(x, y, val):
            # val = x / y
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
                # 把 root_x 挂到 root_y 下面
                parent[root_x] = root_y
                # 推导 root_x / root_y 的权重:
                # 已知: x / root_x = weight[x], y / root_y = weight[y], x / y = val
                # 求: root_x / root_y
                # root_x / root_y = (x / weight[x]) / (y / weight[y])
                #                 = (x / y) * (weight[y] / weight[x])
                #                 = val * weight[y] / weight[x]
                weight[root_x] = val * weight[y] / weight[x]
                
        # 1. 遍历等式，构建带权并查集
        for (u, v), val in zip(equations, values):
            union(u, v, val)
            
        # 2. 处理查询
        ans = []
        for u, v in queries:
            if u not in parent or v not in parent:
                ans.append(-1.0)
            else:
                root_u = find(u)
                root_v = find(v)
                if root_u != root_v:
                    ans.append(-1.0) # 不在同一个连通分量中，无法计算
                else:
                    # 已知 u / root = weight[u], v / root = weight[v]
                    # 所以 u / v = weight[u] / weight[v]
                    ans.append(weight[u] / weight[v])
                    
        return ans

