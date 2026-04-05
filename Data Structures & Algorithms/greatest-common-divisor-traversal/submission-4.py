class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        
        parents = [i for i in range(n)]
        size = [1]*n

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return

            if size[px] < size[py]:
                px, py = py, px
            parents[py] = px
            size[px] += size[py]
        
        factor_map = {}
        for i in range(n):
            x = nums[i]
            f = 2
            while f*f <= x:
                if x%f == 0:
                    if f in factor_map:
                        union(factor_map[f], i)
                    else:
                        factor_map[f] = i
                    while x%f == 0:
                        x //= f
                f += 1
            if x > 1:
                if x in factor_map:
                    union(factor_map[x], i)
                else:
                    factor_map[x] = i

        root0 = find(0)
        for i in range(1,n):
            if find(i) != root0:
                return False
        return True


