class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -=1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal's algorithm
        # 1. 记录每条边的原始索引，并按权重从小到大排序
        # edge 格式: [u, v, weight, original_index]
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])
        new_edges.sort(key=lambda x: x[2])

        # 辅助函数：计算 MST 权重
        def get_mst_weight(ignore_idx = -1, force_idx = -1):
            uf = UnionFind(n)
            total_weight = 0
            if force_idx != -1:
                u, v, w = edges[force_idx]
                uf.union(u, v)
                total_weight += w
            for u, v, w, idx in new_edges:
                if idx == ignore_idx:
                    continue
                if uf.union(u, v):
                    total_weight += w
            return total_weight if uf.count == 1 else float('inf')
        
        # 2. 计算基准 MST 权重
        base_weight = get_mst_weight()
        critical = []
        pesudo_critial = []

        for i in range(len(edges)):
            if get_mst_weight(ignore_idx = i) > base_weight:
                critical.append(i)
            elif get_mst_weight(force_idx = i) == base_weight:
                pesudo_critial.append(i)
        
        return [critical, pesudo_critial]

"""
这两者都是用来解决**最小生成树（MST）**问题的贪心算法，把它们区别搞明白，核心就在于看问题的**视角**和**扩张方式**不同。

用一句“人话”总结：

* **Kruskal 算法**：**全局挑最便宜的边**（看边，拼图式造树）。
* **Prim 算法**：**从起点向外滚雪球**（看点，扩张式造树）。

---

## 核心区别拆解

### 1. 视角不同：选“边”还是选“点”？

* **Kruskal（看边）**：它眼里只有**边**。把所有的边按便宜程度（权重）排个序，不管连接哪个节点，只要**最便宜**且**不会形成环**（用并查集检查），我就选它。
* **Prim（看点）**：它眼里只有**节点**。先随便选一个起点，把它标记为“已占领”。然后看所有“已占领节点”能延伸出去的所有边里，**哪条边能连接到一个“未占领节点”且成本最低**，就把那个新节点拉下水。

---

### 2. 生长过程：森林合并 vs 单树扩张

* **Kruskal**：在中间过程中，图里会同时出现很多互不相连的小树（**森林**）。随着加入的边越来越多，这些小树才渐渐合并成一棵大树。
* **Prim**：从头到尾只有**一棵树**。它像滚雪球一样，从小大本营开始，一圈一圈往外吃新节点，时刻保证当前选中的都是一棵连通的树。

---

### 3. 核心工具与实现逻辑

* **Kruskal**：
* **工具**：**排序 + 并查集（Union-Find）**。
* **逻辑**：先把所有边排序，按顺序遍历边；如果边的两个端点不在同一个集合里，就用并查集 `union` 起来。


* **Prim**：
* **工具**：**小顶堆 / 优先队列（Min-Heap）**。
* **逻辑**：维持一个候选边堆，每次从堆里弹出现在能连到的最便宜的边，加入新节点后，再把这个新节点能延伸出的新边压入堆中。



---

## 一图对比

| 对比维度 | Kruskal 算法 | Prim 算法 |
| --- | --- | --- |
| **核心视角** | 看**边** | 看**点** |
| **中间状态** | 很多小树组成的**森林**，最后拼起来 | 一棵从小到大**不断膨胀**的树 |
| **核心数据结构** | **并查集** (Union-Find) | **小顶堆** (Min-Heap / Priority Queue) |
| **时间复杂度** | $O(E \log E)$ （主要卡在给边排序） | $O(E \log V)$ （带堆优化） |
| **最佳使用场景** | **稀疏图**（边少、点多，如航班航线网） | **稠密图**（边极多、关系复杂，如电路板设计） |

---

## 什么时候用哪个？

在刷题和实际工程中，做选择非常简单：

1. **写起来最爽、面试最常用**：**Kruskal**。配合并查集，代码逻辑极其直接（排序 $\rightarrow$ 遍历 $\rightarrow$ `union`），逻辑非常顺手，也是绝大多数 MST 题目的首选。
2. **图非常稠密时**：当边数 $E$ 接近 $V^2$（即任意两点间几乎都有边）时，给所有边排序会非常耗时，这时用堆优化的 **Prim** 性能更好。
"""
