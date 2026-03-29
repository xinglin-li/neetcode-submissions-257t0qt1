class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        # 只要 n > 1 且存在 1，就必定不连通
        if 1 in nums:
            return False
        
        # ---- 并查集 Union-Find ----
        parent = list(range(n))
        size = [1] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            # 按 size 合并，尽量保持树浅
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]
        
        # ---- factor_map: 质因子 -> 第一次出现这个因子的 index ----
        factor_map = {}  # key: prime factor, value: index
        
        # 对每个 nums[i] 做质因子分解，并通过共同质因子 union
        for i, val in enumerate(nums):
            x = val
            f = 2
            # 分解到 sqrt(x)
            while f * f <= x:
                if x % f == 0:
                    # 只要当前数有质因子 f，就尝试通过 f 把它和别人 union
                    if f in factor_map:
                        union(i, factor_map[f])
                    else:
                        factor_map[f] = i
                    # 把所有 f 都除干净，避免重复处理
                    while x % f == 0:
                        x //= f
                f += 1
            # 此时如果 x > 1，说明还剩一个大质因子
            if x > 1:
                if x in factor_map:
                    union(i, factor_map[x])
                else:
                    factor_map[x] = i
        
        # ---- 检查所有 index 是否都在同一个连通分量 ----
        root0 = find(0)
        for i in range(1, n):
            if find(i) != root0:
                return False
        return True