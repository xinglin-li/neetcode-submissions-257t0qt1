class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        parent = list(range(n))
        size = [1]*n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a,b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]
        
        factor_map = {}
        for i, val in enumerate(nums):
            x = val
            f = 2
            while f*f <= x:
                if x % f == 0:
                    if f in factor_map:
                        union(i, factor_map[f])
                    else:
                        factor_map[f] = i
                    while x % f == 0:
                        x //= f
                f += 1
            if x > 1:
                if x in factor_map:
                    union(i, factor_map[x])
                else:
                    factor_map[x] = i
                    
        root0 = find(0)
        for i in range(1, n):
            if find(i) != root0:
                return False
        return True

            
