class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        ok1 = ok2 = ok3 = False
        for triplet in triplets:
            a, b, c = triplet
            if a > x or b > y or c > z:
                continue
            if a == x:
                ok1 = True
            if b == y:
                ok2 = True
            if c == z:
                ok3 = True
        return ok1 and ok2 and ok3
