class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # This is a tricky question
        x, y, z = target
        ok1 = ok2 = ok3 = False
        
        for a, b, c in triplets:
            # 过滤掉会导致超出 target 的 triplet（不可用）
            if a > x or b > y or c > z:
                continue
            
            # 按维度检查是否可以提供 coverage
            if a == x:
                ok1 = True
            if b == y:
                ok2 = True
            if c == z:
                ok3 = True
        
        return ok1 and ok2 and ok3