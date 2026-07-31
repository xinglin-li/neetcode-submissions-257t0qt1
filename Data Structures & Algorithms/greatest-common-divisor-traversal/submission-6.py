from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n  # 连通分量的数量

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1
            return True
        return False

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        # 1. 特殊情况：如果只有一个数，不需要任何跳跃，直接连通
        if n == 1:
            return True

        uf = UnionFind(n)
        # 记录映射：质因子 -> 第一次包含该质因数的下标
        prime_to_index = {}

        for i, num in enumerate(nums):
            # 2. 特殊情况：如果数组长度 > 1 且包含 1，1 无法与任何数连通
            if num == 1:
                return False

            # 3. 分解质因数
            d = 2
            temp = num
            while d * d <= temp:
                if temp % d == 0:
                    # 如果这个质因子之前出现过，将当前下标与之前的下标合并
                    if d in prime_to_index:
                        uf.union(i, prime_to_index[d])
                    else:
                        prime_to_index[d] = i
                    
                    # 除尽该质因子
                    while temp % d == 0:
                        temp //= d
                d += 1

            # 处理大于 sqrt(num) 的最后一个质因子
            if temp > 1:
                if temp in prime_to_index:
                    uf.union(i, prime_to_index[temp])
                else:
                    prime_to_index[temp] = i

        # 4. 检查是否所有下标都连通（只剩 1 个连通分量）
        return uf.count == 1